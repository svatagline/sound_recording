const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");

const client = new Client({
  authStrategy: new LocalAuth(), // saves session
  puppeteer: {
    headless: true,
  },
});

// 📱 Numbers must include country code (India = 91)
const numbers = ["919XXXXXXXXX", "918XXXXXXXXX", "917XXXXXXXXX"];

// 💬 Message to send
const MESSAGE = "Hello 👋 This is a test message";

// ⏱️ 30 seconds interval
const INTERVAL = 30 * 1000;

// QR Code
client.on("qr", (qr) => {
  console.log("Scan QR Code to login");
  qrcode.generate(qr, { small: true });
});

// Ready
client.on("ready", async () => {
  console.log("✅ WhatsApp Logged In");

  for (let i = 0; i < numbers.length; i++) {
    const chatId = `${numbers[i]}@c.us`;

    try {
      await client.sendMessage(chatId, MESSAGE);
      console.log(`📨 Message sent to ${numbers[i]}`);
    } catch (err) {
      console.error(`❌ Failed to send to ${numbers[i]}`, err.message);
    }

    // Wait 30 seconds before next message
    if (i < numbers.length - 1) {
      console.log("⏳ Waiting 30 seconds...");
      await new Promise((res) => setTimeout(res, INTERVAL));
    }
  }

  console.log("🎉 All messages sent");
});

client.initialize();
