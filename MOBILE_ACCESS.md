# Access AlgoSphere on Your Phone

## Quick Start

### 1. Find Your Computer's IP Address

**On Mac:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

**On Windows:**
```bash
ipconfig
```

**On Linux:**
```bash
hostname -I
```

Look for an IP address like `192.168.x.x` or `10.0.x.x`

### 2. Start the Servers

**Terminal 1 - Start Flask Backend:**
```bash
cd /tmp/cc-agent/65007529/project
python server.py
```

**Terminal 2 - Start React Frontend:**
```bash
cd projects/AlgoSphere-frontend
npm run dev
```

### 3. Access on Your Phone

Make sure your phone is on the **same WiFi network** as your computer.

**Open your phone's browser and visit:**

- Frontend: `http://YOUR_IP_ADDRESS:5173`
- Backend API: `http://YOUR_IP_ADDRESS:5000`

Example: If your IP is `192.168.1.100`, visit `http://192.168.1.100:5173`

## Troubleshooting

### Can't Connect?

1. **Check firewall settings** - Allow ports 5000 and 5173
2. **Verify same WiFi** - Both devices must be on the same network
3. **Disable VPN** - VPNs can block local network access
4. **Try different IP** - Use the WiFi network IP (starts with 192.168 or 10.0)

### For Mac Users - Allow Network Access:

```bash
# Allow port 5173 (Vite)
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/local/bin/node
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblock /usr/local/bin/node

# Allow port 5000 (Flask)
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/bin/python3
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblock /usr/bin/python3
```

### For Windows Users - Allow Network Access:

1. Open Windows Defender Firewall
2. Click "Allow an app through firewall"
3. Allow Node.js and Python on Private networks

## Production Deployment (Optional)

For public access beyond your local network, consider:

1. **Deploy to Vercel/Netlify** (Frontend)
2. **Deploy to Railway/Render** (Backend)
3. **Use ngrok** for temporary public URLs

### Quick ngrok Setup:

```bash
# Install ngrok
# Visit https://ngrok.com and sign up

# Expose frontend
ngrok http 5173

# Expose backend (in another terminal)
ngrok http 5000
```

You'll get public URLs that work from anywhere.
