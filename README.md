# 🚀 TikTok Ultimate Automation

**Professional Grade TikTok Engagement Tool - v2.0**

The most advanced TikTok automation bot combining **Zefoy** and **Zefame** services with a stunning, professional-grade terminal UI. Run multiple services simultaneously with real-time statistics and monitoring.

---

## ✨ Features

### 🎨 Beautiful UI
- **Modern Terminal Interface** - Professional-grade TUI built with Rich library
- **Real-time Dashboard** - Live statistics, activity logs, and service monitoring
- **Color-coded Status** - Instant visual feedback for all operations
- **Progress Tracking** - See exactly what's happening in real-time

### ⚡ Dual-Service Integration
- **Zefoy Services**: Followers, Hearts, Comment Hearts, Views, Shares, Favorites, Livestream
- **Zefame Services**: Views, Followers, Likes, Shares, Favorites
- **Simultaneous Execution** - Run multiple services at the same time
- **Smart Threading** - Efficient parallel processing

### 📊 Advanced Features
- **Live Statistics Dashboard**
  - Total delivered
  - Success/failure rates
  - Runtime tracking
  - Per-service breakdown
- **Intelligent Error Handling**
  - Automatic retries
  - Rate limit detection
  - Connection recovery
- **Activity Logging**
  - Real-time event feed
  - Color-coded messages
  - Detailed progress updates

---

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- Chrome browser installed
- Internet connection

### Quick Install

```bash
# Clone or download the files
cd tiktok_ultimate

# Install dependencies
pip install -r requirements.txt

# Or install manually
pip install rich selenium webdriver-manager requests colorama
```

---

## 🎯 Usage

### Basic Usage

```bash
python tiktok_ultimate.py
```

### Step-by-Step Guide

1. **Launch the Tool**
   ```bash
   python tiktok_ultimate.py
   ```

2. **Login**
   - Username: `admin`
   - Password: `admin`
   - Browser will automatically initialize

3. **Select Services**
   - Choose from Zefoy (Z1-Z7) and Zefame (F1-F5)
   - Examples:
     - `Z1,F2` - Zefoy Followers + Zefame Followers
     - `Z4,F1,Z5` - Zefoy Views + Zefame Views + Zefoy Shares
     - Press Enter to use all available services

4. **Configure Targets**
   - Set desired amount for each service
   - Example: `1000` for 1000 followers

5. **Enter Video URL**
   - Paste your TikTok video link
   - Tool automatically extracts video ID

6. **Solve CAPTCHA**
   - Complete the CAPTCHA on Zefoy
   - May need to watch a short ad

7. **Watch the Magic** ✨
   - Live dashboard shows real-time progress
   - Multiple services run simultaneously
   - Statistics update automatically

---

## 🎨 UI Preview

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      TIKTOK ULTIMATE AUTOMATION                           ║
║                    Professional Grade Engagement Tool                     ║
╚═══════════════════════════════════════════════════════════════════════════╝

┌─ STATISTICS ──────────────┐  ┌─ ACTIVE SERVICES ──────────┐
│                            │  │ Service      Type   Status │
│ RUNTIME     00:15:32       │  │ Followers    Zefoy  ● Running│
│ DELIVERED   1,250          │  │ Views        Zefame ● Running│
│ SUCCESS     42 cycles      │  │ Shares       Zefoy  ● Running│
│ FAILED      3 cycles       │  │                             │
│ RATE        93.3%          │  │                             │
└────────────────────────────┘  └─────────────────────────────┘

┌─ ACTIVITY LOG ────────────────────────────────────────────────────────────┐
│ ● Zefoy Followers: +25 (275/1000)                                        │
│ ● Zefame Views: +150 (450/1000)                                          │
│ ● Zefoy Shares: +25 (125/500)                                            │
│ ● Zefoy Followers: +25 (300/1000)                                        │
│ ● Zefame Views: +150 (600/1000)                                          │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Service Details

### Zefoy Services (Browser-Based)
| Code | Service | Rate | Cooldown |
|------|---------|------|----------|
| Z1 | Followers | ~25 per cycle | ~2-5 min |
| Z2 | Hearts | ~25 per cycle | ~2-5 min |
| Z3 | Comment Hearts | ~25 per cycle | ~2-5 min |
| Z4 | Views | ~25 per cycle | ~2-5 min |
| Z5 | Shares | ~25 per cycle | ~2-5 min |
| Z6 | Favorites | ~25 per cycle | ~2-5 min |
| Z7 | Livestream | ~25 per cycle | ~2-5 min |

### Zefame Services (API-Based)
| Code | Service | Rate | Cooldown |
|------|---------|------|----------|
| F1 | Views | Variable | ~1 min |
| F2 | Followers | Variable | ~1 min |
| F3 | Likes | Variable | ~1 min |
| F4 | Shares | Variable | ~1 min |
| F5 | Favorites | Variable | ~1 min |

---

## ⚙️ Configuration

### Service Selection Examples

**Single Service:**
```
Select services: Z1
```

**Multiple Services:**
```
Select services: Z1,F2,Z4,F1
```

**All Services:**
```
Select services: [Press Enter]
```

### Target Configuration

- Set realistic targets (100-10,000 recommended)
- Higher targets = longer runtime
- Services run independently

---

## 🛡️ Safety Features

- **Automatic Browser Restart** - Detects long rate limits (e.g., 525592 minutes) and automatically restarts browser with new user agent and flushed DNS
- **User Agent Rotation** - 6 different user agents to avoid detection
- **DNS Flushing** - Clears DNS cache on browser restart
- **Rate Limit Detection** - Automatic cooldown when limits hit
- **Error Recovery** - Auto-retry on failures
- **Ad Handler** - Manages Zefoy advertisements
- **Thread Safety** - Proper synchronization
- **Graceful Shutdown** - Clean exit on Ctrl+C
- **French/English Support** - Detects "Commande passée avec succès" and "success" messages

---

## 🔥 Performance Tips

1. **Start Small** - Test with 100-500 targets first
2. **Mix Services** - Use both Zefoy and Zefame for faster results
3. **Stable Connection** - Ensure reliable internet
4. **Monitor Dashboard** - Watch for errors/warnings
5. **Be Patient** - Services have cooldowns

---

## 🐛 Troubleshooting

### Browser Won't Start
```bash
# Update webdriver
pip install --upgrade webdriver-manager
```

### CAPTCHA Issues
- Use a different browser profile
- Clear cookies
- Try during off-peak hours

### Connection Timeout
- Check internet connection
- Restart the tool
- Try fewer simultaneous services

### Long Rate Limits (525592 minutes)
- Tool automatically detects and restarts browser
- New user agent and DNS flush applied
- Service automatically reconfigured
- If it happens frequently, use fewer services

### Rate Limits
- Tool automatically handles this
- Wait time shown in activity log
- Reduces stress on servers

### Zefame "Failed" but Working
- Tool now correctly detects French success message
- "Commande passée avec succès" = SUCCESS
- Check activity log for green success messages

---

## 📊 Statistics Explained

- **DELIVERED** - Total engagement delivered across all services
- **SUCCESS** - Number of successful cycles completed
- **FAILED** - Number of failed attempts
- **RATE** - Success percentage (higher is better)
- **RUNTIME** - Total time elapsed

---

## ⚠️ Important Notes

1. **Educational Purpose** - This tool is for educational purposes only
2. **Account Safety** - Use at your own risk
3. **Service Availability** - Some services may be down temporarily
4. **Rate Limits** - Services have built-in cooldowns
5. **Browser Requirement** - Chrome must be installed

---

## 🎯 Best Practices

✅ **DO:**
- Start with small targets to test
- Monitor the dashboard regularly
- Use stable internet connection
- Follow service cooldowns
- Mix Zefoy and Zefame services

❌ **DON'T:**
- Set unrealistic targets (100k+)
- Close browser manually
- Spam same service repeatedly
- Ignore rate limit warnings
- Share your login credentials

---

## 🔄 Update History

### v2.1 (Current) - Critical Fixes
- ✨ **Automatic Browser Restart** - Detects long rate limits (525592+ minutes) and restarts browser
- 🔄 **User Agent Rotation** - 6 different UAs to avoid detection
- 🌐 **DNS Flushing** - Clears DNS on restart for fresh identity
- 🇫🇷 **French Support** - Correctly detects "Commande passée avec succès" as SUCCESS
- 🎯 **Smart Success Detection** - Handles both English and French responses
- 🛡️ **Enhanced Stability** - Better error handling and recovery

### v2.0
- ✨ Complete UI overhaul with Rich library
- 🚀 Dual-service integration (Zefoy + Zefame)
- 📊 Real-time statistics dashboard
- ⚡ Simultaneous service execution
- 🛡️ Enhanced error handling
- 🎨 Professional terminal interface

### v1.0
- Basic Zefoy automation
- Simple CLI interface

---

## 💡 Tips & Tricks

### Maximize Speed
```
Select: Z1,F2,Z4,F1,Z5,F4
```
Run complementary services together for fastest results.

### Focus on One Type
```
Select: Z1,F2
```
Stack similar services (e.g., followers) for concentrated growth.

### Balanced Approach
```
Select: Z1,Z4,Z5,F1
```
Mix different engagement types for natural-looking growth.

---

## 🤝 Support

Having issues? Check:
1. Requirements are installed: `pip list`
2. Chrome is installed and updated
3. Internet connection is stable
4. No VPN/proxy interference

---

## 📜 License

This project is for **educational purposes only**. Use responsibly.

---

## 🌟 Credits

**Created by @Crypted**

- Combines Zefoy automation
- Integrates Zefame API
- Built with Python & Rich
- Designed for performance

---

## 🚀 Quick Start Cheat Sheet

```bash
# 1. Install
pip install -r requirements.txt

# 2. Run
python tiktok_ultimate.py

# 3. Login
Username: admin
Password: admin

# 4. Select Services
Example: Z1,F2,Z4

# 5. Set Targets
Example: 1000

# 6. Enter Video URL
Paste TikTok link

# 7. Solve CAPTCHA & Watch!
```

---

**Made with ❤️ by @Crypted | TikTok Ultimate v2.0**
