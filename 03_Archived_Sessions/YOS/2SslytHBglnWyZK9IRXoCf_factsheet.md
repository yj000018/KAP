---
uid: 2SslytHBglnWyZK9IRXoCf
session_url: https://manus.im/app/2SslytHBglnWyZK9IRXoCf
session_title: "Customs Non-Receipt Claim Letter – Order PK26001553 (1987 EUR)"
date: 2026-05-31
project: "Customs Dispute / Order PK26001553"
language: mixed
depth: quick
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:32
referenced_sessions: []
referenced_artifacts: ["invoice_PK26001553.pdf", "signature_image.png", "claim_letter_PK26001553.pdf"]
referenced_urls: ["https://manus.im/app/2SslytHBglnWyZK9IRXoCf"]
input_files: ["invoice_PK26001553.pdf", "signature.tiff"]
message_count: 18
---

# Customs Non-Receipt Claim Letter – Order PK26001553 (1987 EUR)

> **Session:** [2SslytHBglnWyZK9IRXoCf](https://manus.im/app/2SslytHBglnWyZK9IRXoCf) | **Date:** 2026-05-31 | **Project:** Customs Dispute / Order PK26001553 | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick needed a formal PDF letter to a Lithuanian seller certifying non-receipt of a food order (PK26001553, 1 987,03 EUR) due to Swiss customs blockage. Manus extracted order details from an uploaded invoice PDF, generated the letter, then refined it by removing post-signature content and embedding a handwritten signature image. The final output is a signed, ready-to-send formal claim letter requesting full refund of goods and customs fees.

### 🎯 Context & Intent
A food order placed with UAB "Poilsio sprendimai" (Lithuania) was blocked and rejected by Swiss customs, leaving Yannick without the goods. He needed a professional written document to formally certify non-receipt, request a full refund (goods + shipping), and address the customs fees reimbursement — suitable for direct transmission to the seller.

### ✅ What Was Done
1. Read and parsed the uploaded invoice PDF to extract all order details (seller, buyer, reference, amount, date)
2. Generated a formal PDF claim letter in English certifying non-receipt due to Swiss customs issues, including refund demand
3. Received instruction to clean post-signature content and embed handwritten signature
4. Handled TIFF format failure — advised user to convert to PNG/JPG
5. Successfully received the converted signature image
6. Updated the PDF: removed all post-signature text and integrated the handwritten signature

### 💡 Key Insights
- TIFF format is not reliably supported by Manus upload interface — PNG/JPG required for image uploads
- Order reference: **PK26001553**, dated 06.05.2026, amount **1 987,03 EUR**
- Customs blockage involved food products / salt deemed non-compliant for Swiss import
- The letter covers two distinct reimbursement tracks: (1) seller refund for goods+transport, (2) customs fees via carrier/customs authority
- Yannick signs as **Jolliet Yannick**, Switzerland

### 📦 Outputs Produced
- **[doc]** `claim_letter_PK26001553.pdf`: Signed formal letter to UAB "Poilsio sprendimai" certifying non-receipt of order PK26001553, requesting full refund of 1 987,03 EUR and customs fee reimbursement, with embedded handwritten signature

### ⚠️ Open Items & Blockers
- [INCERTAIN] Actual customs fees amount not specified in the letter — may need to be added once Yannick has the official customs invoice
- [INCERTAIN] No confirmation that the letter was successfully sent to the seller
- [INCERTAIN] Whether the seller's contact details (email/address) are sufficient for formal legal correspondence
- Whether Swiss customs will automatically refund fees or if a separate formal request to customs/carrier is required

### 🔁 Next Steps
1. Send the signed PDF letter to UAB "Poilsio sprendimai" via email and/or registered mail
2. Obtain the official Swiss customs fee invoice and initiate a separate refund claim with the carrier (e.g., DHL/FedEx/Post CH)
3. Follow up with seller within 7–14 days if no refund acknowledgement received
4. If no response, escalate via PayPal/credit card chargeback or Lithuanian consumer protection authority

### 🔗 Links & References
- 🔗 session:`2SslytHBglnWyZK9IRXoCf`
- 📄 artifact: Invoice PDF (uploaded) — order PK26001553, UAB "Poilsio sprendimai", 06.05.2026
- 📄 artifact: Signature image (uploaded, converted from TIFF to PNG/JPG)
- 📄 artifact: Final claim letter PDF with embedded signature

### 🧠 Resume Hint
The signed PDF claim letter for customs-blocked order PK26001553 (1 987,03 EUR, Lithuanian seller) is complete — next action is sending it to the seller and filing a separate customs fee refund with the carrier.

### 🏷️ Tags
`claim-letter` `customs-dispute` `refund-request` `pdf-generation` `switzerland-import`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 18 messages — 2026-05-31

**[2026-05-31 08:54] USER:** write a quickletter PDF to this seller with reference to all info for this order, cerifying I never received the foods, due to customs issues. And that the way to proceed from here is a full refund of the good purchased + ensuring customs refund me the cuoms fees

**[2026-05-31 08:54] MANUS:** Lu. Je lis le PDF pour extraire les infos de commande, puis je génère la lettre.

**[2026-05-31 08:55] MANUS:** Fait. Voici la lettre PDF certifiant la non-réception de la commande **PK26001553** (1 987,03 EUR) due au blocage douanier, avec la demande de remboursement intégral et la gestion des frais de douane. 

### 📄 Résumé des informations incluses :
* **Vendeur :** UAB "Poilsio sprendimai" (Lituanie)
* **Acheteur :** Jolliet Yannick (Suisse)
* **Facture Réf :** PK26001553 (06.05.2026)
* **Montant :** 1 987,03 EUR
* **Motif :** Blocage et rejet par les douanes suisses (produits alimentaires/sel non conformes à l'importation).
* **Résolution exigée :** Remboursement intégral (biens + transport) + annulation/remboursement des frais de douane associés auprès du transporteur.

Le document est disponible en pièce jointe ci-dessous.

**[2026-05-31 09:05] USER:** good, remove stuff after signature, and add my handwrittent signature attached

**[2026-05-31 09:05] MANUS:** Le fichier de signature n'a pas été uploadé correctement. Peux-tu le renvoyer ?

**[2026-05-31 09:08] USER:** good, remove stuff after signature, and add my handwrittent signature attached

**[2026-05-31 09:08] MANUS:** Le fichier TIFF échoue à l'upload à nouveau. Essaie de le convertir en PNG ou JPG avant de l'envoyer — le format TIFF n'est pas toujours supporté par l'interface.

**[2026-05-31 09:09] MANUS:** Signature reçue. Je mets à jour la lettre — suppression du texte post-signature + intégration de la signature manuscrite.

**[2026-05-31 09:09] MANUS:** Mis à jour. Texte post-signature supprimé, signature manuscrite intégrée.
