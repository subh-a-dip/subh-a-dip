# 🐍 3D Realistic Snake Game

A modern, feature-rich 3D Snake game that works on both mobile and PC with realistic graphics and advanced gameplay mechanics.

## 🎮 Features

### Visual & Graphics
- **3D Isometric Graphics** with realistic lighting and shadows
- **Particle Effects** when eating food
- **Gradient Backgrounds** and glowing effects
- **Responsive Design** for mobile and desktop
- **Smooth Animations** and visual feedback

### Gameplay Features
- **Multiple Food Types** with different point values
- **Power-ups System**:
  - 🚀 Speed Boost (temporary speed increase)
  - 🐌 Slow Motion (easier control)
  - 💎 Double Points (instant score bonus)
- **Progressive Difficulty** - speed increases with level
- **High Score System** with local storage
- **Pause/Resume** functionality

### Controls
- **PC**: WASD or Arrow Keys, Space (pause), R (restart)
- **Mobile**: Touch controls with swipe gestures
- **Cross-Platform** compatibility

## 🚀 Quick Start

### Method 1: Double-click to play
1. Double-click `run_game.bat`
2. Game opens automatically in your browser
3. Start playing!

### Method 2: Manual start
1. Open terminal/command prompt
2. Navigate to the game folder
3. Run: `python server.py`
4. Open browser to `http://localhost:8000`

## 🎯 How to Play

1. **Move**: Use WASD/Arrow keys or swipe on mobile
2. **Eat Food**: Guide snake to colored food items
3. **Avoid Walls**: Don't hit the boundaries
4. **Avoid Self**: Don't run into your own tail
5. **Collect Power-ups**: Grab special items for bonuses
6. **Score Points**: Normal food = 10pts, Special food = 20pts

## 🏆 Scoring System

- **Normal Food**: 10 points
- **Special Food**: 20 points (golden/glowing items)
- **Double Points Power-up**: Instant 50 point bonus
- **Level Up**: Every 100 points increases level and speed

## 📱 Mobile Features

- **Touch Controls**: Tap directional buttons
- **Swipe Gestures**: Swipe to change direction
- **Responsive Layout**: Optimized for all screen sizes
- **Performance Optimized**: Smooth gameplay on mobile devices

## 🔧 Technical Details

- **Frontend**: HTML5 Canvas, JavaScript ES6+
- **Backend**: Python HTTP Server
- **Graphics**: 2D Canvas with 3D effects
- **Storage**: LocalStorage for high scores
- **Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)

## 🌐 Network Play

Share the game with others on your network:
1. Start the server
2. Share the network URL shown in console
3. Others can play from their devices

## 🎨 Customization

The game is built with modular code for easy customization:
- Modify colors in `game.js`
- Adjust game speed and difficulty
- Add new power-up types
- Change visual effects

## 🐛 Troubleshooting

**Game won't start?**
- Ensure Python is installed
- Check if port 8000 is available
- Try running `python server.py 8080` for different port

**Performance issues?**
- Close other browser tabs
- Reduce browser zoom level
- Update your browser

## 📄 License

Open source - feel free to modify and share!

---

**Enjoy the game! 🎮🐍**