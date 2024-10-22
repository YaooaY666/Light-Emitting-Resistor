# H.-S.-Greene
## 🚸 Challenge One: Distracting Shadowmire's Son

### Step 1: Overview of the Game

The challenge required us to improve upon an existing web-based **Snake game** that would effectively distract Shadowmire's son. We used **JavaScript** and **HTML** to build on the classic game by adding new features and enhancements. The goal was to make the game more fun, engaging, and challenging, ensuring that it could hold the player's attention for as long as possible.

### Step 2: Improvements and Additions

Instead of building the game from scratch, we improved upon the original **Snake game**. The original version included basic features such as a 20x20 board, apples, and a snake that the player controls. Below are the key improvements and additions:

1. **Hunters**:

   - We introduced **hunters** that move around the board to challenge the player. Hunters are added every 5 points, increasing the difficulty level and making the game more engaging. Hunters have random movement, which makes avoiding them more exciting.

2. **Obstacles**:

   - **Obstacles** were added to the board to limit movement options and increase the challenge. Obstacles are placed randomly at the beginning of the game, making navigation more difficult.

3. **Dynamic Scoreboard**:

   - We implemented a **scoreboard** to keep track of the player's current score and highest score. The highest score is saved using `localStorage` to encourage players to beat their previous records.

4. **Special Messages**:

   - Added special messages like **"Yummy!"** or **"Rise and Shine!"** that appear when the snake eats an apple or starts a new game. These messages make the game more interactive and fun.

5. **Increased Difficulty**:

   - As the player progresses, more hunters are introduced, which makes the game increasingly challenging. The difficulty ramps up as the score increases, ensuring the game remains engaging.

### Step 3: Game Logic and Movement

- The **snake** is controlled using arrow keys, and the game runs at a frame rate of **60 FPS**.
- Each **hunter** has a preferred direction of movement, which changes randomly to keep the gameplay unpredictable.
- The **board** is represented as a 2D array, where different values indicate the presence of elements like the snake, apple, hunter, or obstacles.

### Thought Process Behind the Solution

The main goal was to take a classic game that was already familiar and improve it to create a more engaging and challenging experience. We focused on:

- **Adding Challenge**: Introducing hunters and obstacles added more complexity to the game, making it more difficult and enjoyable.
- **Progressive Difficulty**: By adding more hunters as the score increased, we ensured the game would get progressively harder, keeping it interesting.
- **Visual and Interactive Elements**: Fun messages, a scoreboard, and moving elements were included to make the game visually attractive and immersive.

## 🔐 Challenge Two - Winning Over Shadowmire's Wife

### Step 1: Creating the Heart Shape

The first step was to create the central heart shape, which serves as the focal point of the plot. Using **parametric equations**, the heart was drawn with smooth, symmetric curves to convey a feeling of love and warmth. The heart is colored in **red**, symbolizing passion and affection, making it the main visual element.

### Step 2: Adding Animations

To bring the heart to life, we added several animations:

- **Pulsating Heart**: The central heart shape was animated to pulsate slightly, creating a "beating" effect. This symbolizes the beating of one's heart for a loved one, adding a lifelike quality to the visual.
- **Text Animation**: The central text, "Love You Forever," was animated with subtle changes, making it feel alive and expressive, enhancing the romantic mood of the plot.

### Step 3: Romantic Annotations

Around the heart, we strategically placed **romantic phrases** such as "Love You Forever," "Together Forever," and "Endless Love." These annotations help create a sense of surrounding love and devotion, enhancing the emotional impact of the plot.

### Step 4: Decorative Elements for a Magical Atmosphere

To enhance the romantic atmosphere, we added multiple decorative elements:

- **Decorative Hearts with Gradient Effect**: Smaller hearts were placed around the main heart, with different levels of transparency to create a gradient-like effect. These hearts float gently, adding a sense of motion and magic.
- **Gold Particles**: We scattered gold particles throughout the plot to create a sparkling, magical effect. The particles move gently, contributing to the whimsical atmosphere.
- **Shooting Stars**: To symbolize wishes and dreams, shooting stars were added to the plot. These stars move across the screen, adding an element of fantasy and wonder.

### Step 5: Pulsing Halo

A **pulsing halo** was added around the central heart to emphasize it. The halo pulses in size over time, giving the impression of a glowing aura of love and making the heart stand out even more.

### Step 6: Color Choices and Aesthetic Styling

The overall color scheme was carefully chosen to create a romantic and gentle atmosphere:

- The **background** is colored in a soft pink to set a romantic tone.
- The **plot spines** are styled in pink and red to complement the heart and maintain consistency in the visual theme.
