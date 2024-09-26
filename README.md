# Multiple Pendulums Simulator

This project is a Multiple Pendulums Simulator built using Python's Tkinter library and optimized with NumPy for efficient computation. It visualizes n double pendulums with a rainbow gradient, demonstrating their motion in real-time.

## Customization

You can customize the following parameters directly in the script:

- **`g`**: Gravitational acceleration (default: `9.81`).
- **`l1`, `l2`**: Lengths of the pendulum arms (default: `1.0` each).
- **`m1`, `m2`**: Masses of the pendulum bobs (default: `1.0` each).
- **`num_pendulums`**: Number of pendulums to simulate (default: `350`).
- **`t_step`**: Time step for the simulation (default: `0.005`).
- **`diff`**: Initial difference in angles for pendulums (default: `0.00001`).
- **`scale`**: Scaling factor for visualization (default: `150`).
- **`offset_x`, `offset_y`**: Canvas offset positions (default: `300` each).
- **Color Scheme**: Modify the `get_rainbow_color` function to change the color gradient or implement different coloring techniques without altering other parts of the code.
