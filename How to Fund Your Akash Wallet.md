# 💰 How to Fund Your Akash Wallet (AKT Tokens)

To deploy your AI assistant on the **Akash Network**, you must fund your **Akash wallet** with the native token: **AKT**.

This guide walks you through the two most common methods: **decentralized (DEX)** and **centralized (CEX)**.

---

## 🔑 1. Prerequisites

- ✅ You must already have an **Akash wallet address** (e.g., `akash1vn06yc...`)
- ✅ You must have a **Keplr Wallet** or equivalent Cosmos-compatible wallet
- ✅ Optionally: a Coinbase or Kraken account (for fiat on-ramp)

---

## 🔄 2. Fund via Decentralized Exchange (DEX)

Recommended for privacy and decentralization. This involves using **OSMO** (Osmosis DEX) or similar.

### 🌐 Steps:

1. **Buy ATOM or USDC** on any exchange (e.g., Coinbase)
2. **Send to your Keplr Wallet** (ensure you’re on the Cosmos Hub network)
3. **Go to Osmosis DEX**: [https://app.osmosis.zone/](https://app.osmosis.zone/)
4. **Swap ATOM → AKT**
5. **Bridge to Akash Wallet** within Keplr

⚠️ You must select the **Akash network** when sending AKT to your deployment wallet.

---

## 🏦 3. Fund via Centralized Exchange (CEX)

This option is simpler but may involve more KYC/fees.

### 🔁 Supported CEXes:
- [Coinbase](https://coinbase.com) (buy ATOM or USDC)
- [Kraken](https://kraken.com) (buy ATOM or USDT)

### 🪙 Steps:

1. **Buy ATOM** or stablecoin
2. **Withdraw** to your **Keplr Wallet** (Cosmos network)
3. **Swap** using Osmosis or transfer directly if your exchange supports AKT

---

## 🧪 Verify Balance

You can check your Akash wallet balance using:

```
akash query bank balances <your-wallet-address>
```

Or online at [https://akash.bigdipper.live/](https://akash.bigdipper.live/)

---

## 💡 Pro Tips

- Always send a **small test amount first** (e.g., 0.1 AKT)
- Double-check the wallet address prefix is `akash1...`
- You may need ≈ **5–10 AKT** to fund a simple deployment

---

## 🧠 Why AKT?

AKT is used to **pay for compute** on the Akash Network.  
Each deployment deducts micro-payments per block from your wallet’s **escrow account**.

---

**Built for Akash RAG Deployments • Next Shift Consulting**
