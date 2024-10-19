
const WIDTH = 800;
const HEIGHT = 600;

const EMPTY = 0;
const APPLE = 1;
const SNAKE = 2;
const SNAKE_LEFT  = 3;
const SNAKE_RIGHT = 4;
const SNAKE_UP    = 5
const SNAKE_DOWN  = 6;
const HUNTER = 7;
const OBSTACLE = 8;

const PADDING = 0;

const BOARD_SIZE = 20;
const BOARD_CELL_WIDTH  = WIDTH / BOARD_SIZE;
const BOARD_CELL_HEIGHT  = HEIGHT / BOARD_SIZE;

const FPS = 60;

let playingState = false;
let firstTime = true;

let score = 0;
let highestScore = localStorage.getItem('highestScore') || 0;
let hunters = [];

const DIRECTIONS = {};
DIRECTIONS[SNAKE_LEFT] =  {x : -1, y : 0};
DIRECTIONS[SNAKE_RIGHT] =  {x : 1, y : 0};
DIRECTIONS[SNAKE_UP] =  {x : 0, y : -1};
DIRECTIONS[SNAKE_DOWN] =  {x : 0, y : 1};

/**
 * @param {Array<Array<Number>>} board
 *
 * @returns {{x:number, y:number}}
 */
function getRandomPos(board) {
    let x = Math.floor(Math.random()*BOARD_SIZE);
    let y = Math.floor(Math.random()*BOARD_SIZE);
    while(board[y][x] != EMPTY) {
        x = Math.floor(Math.random()*BOARD_SIZE);
        y = Math.floor(Math.random()*BOARD_SIZE);
    }

    return { x, y };
}

/**
 * @param {Array<Array<Number>>} board
 */
function checkSnake(board, vb, ny, nx) {
    nx = propMod(nx, BOARD_SIZE);
    ny = propMod(ny, BOARD_SIZE);

    if(vb !== null) return board[ny][nx] > SNAKE && !vb[ny][nx];

    return board[ny][nx] > SNAKE;
}

function propMod(a, b) {
    return (a % b + b) % b;
}

/**
 * @param {Array<Array<Number>>} board
 * @param {{x:number, y:number}} snakePos
 * @param {{x:number, y:number}} newPos
 * @param {string} dir
 *
 * @returns {boolean} Possible to update the position of the snake
 */
function updateSnakePosition(board, snakePos, newPos, dir) {
    switch(board[newPos.y][newPos.x]) {
        case EMPTY:
            let queue = [];
            const vb = Array(BOARD_SIZE).fill(0).map(_ => Array(BOARD_SIZE).fill(false));
            const curDir = board[snakePos.y][snakePos.x];
            queue.push({...snakePos, dir: curDir});
            while(queue.length > 0) {
                const {x, y, dir} = queue.shift();
                vb[y][x] = true;
                const dp = DIRECTIONS[dir];
                if(dp) {
                    const nx = propMod(x+dp.x, BOARD_SIZE);
                    const ny = propMod(y+dp.y, BOARD_SIZE);
                    if(checkSnake(board, vb, ny, nx)) {
                        const ndir = board[ny][nx];
                        queue.push({x:nx, y:ny, dir: ndir});
                    } else if(queue.length == 0) {
                        board[y][x] = EMPTY;
                    }
                } else {
                    board[y][x] = EMPTY;
                }
            }
            //board[snakePos.y][snakePos.x] = EMPTY;
            board[newPos.y][newPos.x] = dir;
            break;
        case APPLE:
            board[newPos.y][newPos.x] = dir;

            const applePos = getRandomPos(board);
            board[applePos.y][applePos.x] = APPLE;
            // Add a hunter every 5 points
            if (score % 5 === 0) {
              const hunterPos = getRandomPos(board);
              board[hunterPos.y][hunterPos.x] = HUNTER;
              hunters.push(hunterPos);
            }
            score++;
            timeSinceAte = 0;
            break;
        default:
            return false;
    }
    return true;
}

function isOccupied(pos, board) {
    console.log(pos);
    return board[pos.y][pos.x] !== EMPTY;
}

function moveHunters(board) {
    for (let i = 0; i < hunters.length; i++) {
        let hunter = hunters[i];

        // If hunter has no preferred direction, assign one (random)
        if (!hunter.preferredDirection) {
            hunter.preferredDirection = Math.floor(Math.random() * 4)+3; // 0-3
            hunter.steps = 0;
            hunter.stopAt = Math.floor(Math.random() * 5) + 5; // 5-10
        }

        var newPos = { 
            x: (hunter.x + DIRECTIONS[hunter.preferredDirection].x) % BOARD_SIZE, 
            y: (hunter.y + DIRECTIONS[hunter.preferredDirection].y) % BOARD_SIZE
        };

        // Wrap around board boundaries
        if (newPos.x < 0) newPos.x = BOARD_SIZE - 1;
        if (newPos.y < 0) newPos.y = BOARD_SIZE - 1;

        var tries = 0;
        // Check if new position is occupied
        while (isOccupied(newPos, board) && tries < 4 || hunter.steps > hunter.stopAt) {
            // If blocked, choose a new random direction and try again
            hunter.preferredDirection = Math.floor(Math.random() * 4+3); // Pick new direction
            hunter.steps = 0;
            hunter.stopAt = Math.floor(Math.random() * 5) + 5; // 5-10
            tries++;
        } 
        if (!isOccupied(newPos, board)) {
            // Move the hunter to the new position
            board[hunter.y][hunter.x] = EMPTY; // Clear old position
            hunter.x = newPos.x;
            hunter.y = newPos.y;
            hunter.steps++;

            board[hunter.y][hunter.x] = HUNTER; // Set new position
        }
    }
}

/**
 * @param {CanvasRenderingContext2D} ctx
 * @param {number} x
 * @param {number} y
 * @param {Array<string>} msgs
 */
let currentIndex = 0;
let countInterval = 0;
const displayInterval = 120;

function renderFirstScene(ctx, w, h, highestScore, score) {
    let fontSize = 35;
    const padding = 48;

    // Your backstory array with the score
    let backstory =  firstTime ? [
        'A long time ago in a mystical forest,',
        'a magical tree snake was born, carrying',
        'the hidden secrets of the powerful HKN.',
        '',
        'The snake wandered the enchanted woods,',
        'guarding its knowledge and wisdom.',
        '',
        'But the Blue Smurfs, cunning and relentless,',
        'set their sights on the snake, hunting it down.',
        '',
        'Now, it must escape and protect the secrets.',
        '',
        `The fate of the snake rests on your hands.`,
        `Last time, the snake scored: ${highestScore}`,
        'Press Space to start',
        'Avoid the HUNTERS!'
    ]: [
        `Your Score: ${score}`,
        `Highest Score: ${highestScore}`,
        'Press Space to start',
        'Avoid the HUNTER!'
    ];

    let y = (h - (backstory.length * fontSize + padding)) / 2;


    if (!playingState) {
        // Clear only the background for the backstory, not the whole canvas
        ctx.clearRect(0, 0, w, h); // Clear the entire canvas
        
        ctx.fillStyle = "#96996c";
        ctx.fillRect(0, 0, WIDTH, HEIGHT);
        ctx.font = `${fontSize}px bold`;
        ctx.fillStyle = firstTime ? '#f4f003': 'white';
        // Draw up to the current line of the backstory
        let lineY = y;
        console.log(currentIndex);
        for (let i = 0; i <= currentIndex && i < backstory.length; i++) {
            if (i==12) ctx.fillStyle = 'lightgreen';
            if (i==13) ctx.fillStyle = 'white';
            if (i==14) ctx.fillStyle = 'lightblue';
            const str = backstory[i];
            const x = (w - ctx.measureText(str).width) / 2;
            ctx.fillText(str, x, lineY + padding);
            lineY += fontSize;
        }
        ctx.stroke();

        countInterval++;
        if (currentIndex < backstory.length - 1) {
            if (countInterval >= displayInterval) {
                currentIndex++; // Move to the next line
                countInterval = 0;
            }
        }
    }
}

/**
 * @param {CanvasRenderingContext2D} ctx
 * @param {number} x
 * @param {number} y
 */
let timeSinceBirth = 0;
let selectedMessageBirth = 0;
let timeSinceAte = 0;
let selectedMessageAte = 0;
function renderScore(ctx, x, y) {
    const fontSize = 28;
    const padding = 10;
    const riseAndShineMessages = [
        'Rise and Shine!', 'Good Morning!', 'Wake Up, Snake!', 'Time to slither!', 
        'The forest awaits!', 'A new adventure begins!', 'Stretch those scales!', 
        'The sun is up!', 'Let\'s get moving!', 'Another day, another apple!'
    ];

    const yummyMessages = [
        'Yummy!', 'Delicious!', 'Tasty!', 'Scrumptious!', 'Mouth-watering!', 
        'Delectable!', 'Savory!', 'Appetizing!', 'Lip-smacking!', 'Gourmet treat!'
    ];
    if (timeSinceBirth == 1) {
        selectedMessageBirth = Math.floor(Math.random() * riseAndShineMessages.length);
    }
    if (timeSinceAte > 120) {
        selectedMessageAte = Math.floor(Math.random() * yummyMessages.length);
    }
    const text = timeSinceBirth < 120 
        ? riseAndShineMessages[selectedMessageBirth] 
        : timeSinceAte < 120 
            ? yummyMessages[selectedMessageAte] 
            : `Score: ${score}`; ctx.font = `${fontSize}px bold`;

    ctx.fillStyle = 'black';
    ctx.fillText(text, x + padding, y + padding);
    ctx.stroke();
}

/**
 * @param {CanvasRenderingContext2D} ctx
 */
function renderBoard(ctx, board) {
    for(let row = 0; row < BOARD_SIZE; row++) {
        for(let col = 0; col < BOARD_SIZE; col++) {
            let color = '#c8cc92';
            switch(board[row][col]) {
                case EMPTY:
                    break;
                case APPLE:
                    color = 'red';
                    break;
                case HUNTER:
                    color = 'blue';
                    break;
                case OBSTACLE:
                    color = 'brown'
                    break;
                default:
                    color = 'green';
                    break;
            }
            ctx.fillStyle = color;
            ctx.fillRect(col * BOARD_CELL_WIDTH + PADDING, row*BOARD_CELL_HEIGHT, BOARD_CELL_WIDTH, BOARD_CELL_HEIGHT)
            //ctx.fillStyle = 'white';
            //ctx.strokeRect(col * BOARD_CELL_WIDTH + PADDING, row*BOARD_CELL_HEIGHT, BOARD_CELL_WIDTH, BOARD_CELL_HEIGHT)
        }
    }
    ctx.stroke();
}

(() => {
    const canvas = document.getElementById('game');
    canvas.width = 800;
    canvas.height = 800;

    let snakePos, snakeDir, snakeODir;

    let board = Array(BOARD_SIZE).fill(0).map(_ => Array(BOARD_SIZE).fill(EMPTY));

    const ctx = canvas.getContext("2d");

    let otherMsgs = [];

    window.addEventListener('keydown', (e) => {
        let newDir = undefined;
        let newODir = undefined;
        switch(e.code) {
            case 'ArrowLeft':
                newDir = SNAKE_LEFT;
                newODir = SNAKE_RIGHT;
                break;
            case 'ArrowRight':
                newDir = SNAKE_RIGHT;
                newODir = SNAKE_LEFT;
                break;
            case 'ArrowUp':
                newDir = SNAKE_UP;
                newODir = SNAKE_DOWN;
                break;
            case 'ArrowDown':
                newDir = SNAKE_DOWN;
                newODir = SNAKE_UP;
                break;
            case 'KeyA':
                newDir = SNAKE_LEFT;
                newODir = SNAKE_RIGHT;
                break;
            case 'KeyD':
                newDir = SNAKE_RIGHT;
                newODir = SNAKE_LEFT;
                break;
            case 'KeyW':
                newDir = SNAKE_UP;
                newODir = SNAKE_DOWN;
                break;
            case 'KeyS':
                newDir = SNAKE_DOWN;
                newODir = SNAKE_UP;
                break;
            case 'Space':
                if(!playingState) {
                    playingState = true;
                    firstTime = false;
                    timeSinceBirth = 0;
                    // Reset board
                    otherMsgs = [];
                    board.forEach(r => r.fill(EMPTY));

                    // Add initial obstacles
                    for (let i=0; i<4; i++) {
                        const obstacleX = Math.floor(Math.random() * (BOARD_SIZE-1));
                        const obstacleY = Math.floor(Math.random() * (BOARD_SIZE-1));
                        board[obstacleY][obstacleX] = OBSTACLE;
                        board[obstacleY][obstacleX + 1] = OBSTACLE;
                        board[obstacleY + 1][obstacleX] = OBSTACLE;
                        board[obstacleY + 1][obstacleX + 1] = OBSTACLE;
                    }

                    snakePos = getRandomPos(board);
                    snakeDir = SNAKE_RIGHT;
                    snakeODir = SNAKE_LEFT;

                    board[snakePos.y][snakePos.x] = snakeODir;

                    const applePos = getRandomPos(board);
                    board[applePos.y][applePos.x] = APPLE;
                    score = 0;
                    hunters = [];
                }
                break;
        }
        const dir = DIRECTIONS[newDir];
        if(newDir && !checkSnake(board, null, snakePos.y + dir.y, snakePos.x + dir.x)) {
            snakeDir = newDir;
            snakeODir = newODir;
        }

    });
    let prevTimestamp = 0;
    let frameCount = 0;
    const frame = (timestamp) => {
        //const dt = (timestamp - prevTimestamp) / 1000;
        prevTimestamp = timestamp;
        if(playingState) {
            frameCount += 1;
            timeSinceBirth++;
            timeSinceAte++;
            if(frameCount >= FPS/4) {
                const dir = DIRECTIONS[snakeDir];
                const x = propMod(snakePos.x + dir.x, BOARD_SIZE);
                const y = propMod(snakePos.y + dir.y, BOARD_SIZE);


                if(!updateSnakePosition(board, snakePos, {x, y}, snakeODir)) {
                    if(score > highestScore) {
                        highestScore = score;
                        localStorage.setItem('highestScore', highestScore);
                    }

                    otherMsgs.push(`Current score: ${score}`);
                    playingState = false;
                } else {
                    snakePos.x = x;
                    snakePos.y = y;
                    frameCount = 0;
                    renderBoard(ctx, board);
                    renderScore(ctx, 20, 20);
                }

                if (playingState && frameCount % 20 === 0) { // Move hunters every 30 frames
                    moveHunters(board);
                }
            }
        } else {
            renderBoard(ctx, board);
            renderFirstScene(ctx, WIDTH, HEIGHT, highestScore, score);
        }
        window.requestAnimationFrame(frame);
    }
    window.requestAnimationFrame((timestamp) => {
        prevTimestamp = timestamp;
        window.requestAnimationFrame(frame);
    });
})()
