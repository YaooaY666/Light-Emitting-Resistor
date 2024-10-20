import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as animation
import random
from matplotlib.patches import Circle

def main():
    # Define the heart shape using parametric equations
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    # Plot the heart shape
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('#ffe6f0')  # Set initial gradient-like background color
    main_heart_line, = ax.plot(x, y, color='red', linewidth=3, linestyle='-')

    # Add some initial annotations to make it more romantic
    text = ax.text(0, 0, 'Love You Forever', fontsize=20, fontweight='bold', color='pink',
                   ha='center', va='center', family='cursive')

    # Add multiple text annotations around the heart
    annotations = [
        (-10, 10, 'Always in My Heart'),
        (10, -10, 'Together Forever'),
        (-15, -5, 'Endless Love'),
        (15, 5, 'My One and Only'),
        (3, 10, 'Eternal Flame'),
        (-5, -15, 'Infinite Affection')
    ]
    annotation_texts = []
    for (x_pos, y_pos, message) in annotations:
        annotation_text = ax.text(x_pos, y_pos, message, fontsize=12, fontweight='bold', color='purple',
                                  ha='center', va='center', family='cursive', alpha=0.8)
        annotation_texts.append(annotation_text)

    # Add title and custom styled axes
    ax.set_title("From Shadowmire: To my dear Wife", fontsize=16, fontweight='bold')
    ax.spines['top'].set_color('pink')
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_color('pink')
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_color('red')
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_color('red')
    ax.spines['left'].set_linewidth(2)
    ax.set_xticks([])
    ax.set_yticks([])

    # Add decorative elements like hearts around the main plot with gradient fill
    decorative_hearts_patches = []
    for i in range(6):
        offset = (i + 1) * 0.6
        # Create gradient colors
        colors = [mcolors.to_rgba('pink', alpha=1 - (i * 0.1)) for i in range(6)]
        heart1 = ax.fill_betweenx(y - offset, x + offset - 0.5, x + offset + 0.5, color=colors[i % len(colors)], alpha=0.5)
        heart2 = ax.fill_betweenx(y - offset, x - offset - 0.5, x - offset + 0.5, color=colors[i % len(colors)], alpha=0.5)
        decorative_hearts_patches.append((heart1, heart2))

    # Add particles for decoration
    num_particles = 50
    particles = []
    for _ in range(num_particles):
        x_particle = random.uniform(-20, 20)
        y_particle = random.uniform(-20, 20)
        particle = ax.plot(x_particle, y_particle, 'o', color='gold', markersize=random.uniform(2, 5), alpha=0.7)[0]
        particles.append(particle)

    # Add shooting stars for additional effect
    num_stars = 5
    shooting_stars = []
    for _ in range(num_stars):
        x_star = random.uniform(-20, 20)
        y_star = random.uniform(-20, 20)
        star = ax.plot(x_star, y_star, '*', color='white', markersize=random.uniform(5, 8), alpha=0.8)[0]
        shooting_stars.append(star)

    # Add pulsing halo around the main heart
    halo_circle = Circle((0, 0), 18, color='pink', alpha=0.2, lw=0, fill=True)
    ax.add_patch(halo_circle)

    # Function to update text, heart, particle, shooting star, and halo animations
    def update(frame):
        # Update central heart animation by changing the size slightly over time
        t_dynamic = np.linspace(0, 2 * np.pi, 1000)
        size_factor = 1 + 0.05 * np.sin(0.1 * frame)
        x_dynamic = size_factor * 16 * np.sin(t_dynamic)**3
        y_dynamic = size_factor * (13 * np.cos(t_dynamic) - 5 * np.cos(2 * t_dynamic) - 2 * np.cos(3 * t_dynamic) - np.cos(4 * t_dynamic))
        main_heart_line.set_data(x_dynamic, y_dynamic)

        # Update central text animation
        text.set_text(f"Love You Forever {'.' * (frame % 4)}")

        # Update position of annotations to make them move more gently
        for idx, (x_pos, y_pos, annotation_text) in enumerate(zip([a[0] for a in annotations], [a[1] for a in annotations], annotation_texts)):
            new_x = x_pos + 0.3 * np.sin(0.1 * frame + idx)
            new_y = y_pos + 0.3 * np.cos(0.1 * frame + idx)
            annotation_text.set_position((new_x, new_y))

        # Update decorative hearts to create a gentle floating effect
        for heart_pair in decorative_hearts_patches:
            for heart in heart_pair:
                heart.remove()  # Remove previous hearts

        decorative_hearts_patches.clear()
        for i, offset in enumerate([(i + 1) * 0.6 * size_factor + 0.3 * np.sin(0.1 * frame) for i in range(6)]):
            colors = [mcolors.to_rgba('pink', alpha=1 - (i * 0.1)) for i in range(6)]
            heart1 = ax.fill_betweenx(y - offset, x + offset - 0.5, x + offset + 0.5, color=colors[i % len(colors)], alpha=0.5)
            heart2 = ax.fill_betweenx(y - offset, x - offset - 0.5, x - offset + 0.5, color=colors[i % len(colors)], alpha=0.5)
            decorative_hearts_patches.append((heart1, heart2))

        # Update particles for a floating effect
        for particle in particles:
            new_x_particle = particle.get_xdata() + 0.1 * np.sin(0.1 * frame + random.uniform(0, 2 * np.pi))
            new_y_particle = particle.get_ydata() + 0.1 * np.cos(0.1 * frame + random.uniform(0, 2 * np.pi))
            particle.set_data(new_x_particle, new_y_particle)

        # Update shooting stars to make them shoot across the screen
        for star in shooting_stars:
            new_x_star = star.get_xdata() + 0.5 * np.cos(0.05 * frame + random.uniform(0, 2 * np.pi))
            new_y_star = star.get_ydata() + 0.5 * np.sin(0.05 * frame + random.uniform(0, 2 * np.pi))
            if abs(new_x_star) > 20 or abs(new_y_star) > 20:
                new_x_star = random.uniform(-20, 20)
                new_y_star = random.uniform(-20, 20)
            star.set_data(new_x_star, new_y_star)

        # Update halo size to create a pulsing effect
        halo_circle.set_radius(18 + 2 * np.sin(0.1 * frame))
        halo_circle.set_alpha(0.3 + 0.1 * np.sin(0.1 * frame))

        return [text] + annotation_texts + [main_heart_line] + particles + shooting_stars + [halo_circle]

    # Create an animation for the text, hearts, particles, shooting stars, and halo
    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=100, blit=True)

    # Show the plot
    plt.show()
    
if __name__ == "__main__":
    main()
