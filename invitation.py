from PIL import Image, ImageDraw, ImageFont

# === Create the canvas ===
width, height = 800, 600
background_color = "#ffc0cb"  # Soft pink
invitation = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(invitation)

# === Load fonts (fallback to default if custom ones are missing) ===
try:
    title_font = ImageFont.truetype("arialbd.ttf", 50)
    subtitle_font = ImageFont.truetype("arial.ttf", 30)
    body_font = ImageFont.truetype("arial.ttf", 24)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()

# === Text Colors ===
title_color = "#6a0dad"    # Purple
highlight_color = "#FFD700"  # Gold
text_color = "#4b0082"     # Indigo/purple
rsvp_color = "#8b008b"     # Dark magenta

# === Content ===
couple_names = "Bani 💕 Jay"
date = "Saturday, 25 May 2025"
time = "3:00 PM"
venue = "Botanical Gardens, Harare"
rsvp = "RSVP by May 1st | +263 771 234 567"

# === Draw Text ===
draw.text((width/2, 80), "You're Invited", font=title_font, fill=title_color, anchor="mm")
draw.text((width/2, 160), couple_names, font=title_font, fill=highlight_color, anchor="mm")
draw.text((width/2, 240), date, font=subtitle_font, fill=text_color, anchor="mm")
draw.text((width/2, 280), time, font=subtitle_font, fill=text_color, anchor="mm")
draw.text((width/2, 350), venue, font=body_font, fill=text_color, anchor="mm")
draw.text((width/2, 450), rsvp, font=body_font, fill=rsvp_color, anchor="mm")

# === Save the image ===
invitation.save("bani_jay_wedding_invite.png")
print("💌 Invitation created as 'bani_jay_wedding_invite.png'")

import yagmail

# === Gmail credentials ===
GMAIL_USER = "vdumbatsuro2@gmail.com"  # Replace with your Gmail
GMAIL_PASS = "rzdefvqfjqhjnpku"     # Replace with your App Password

# === Send email function ===
def send_wedding_invite(recipient_email, subject, body, attachment_path):
    try:
        yag = yagmail.SMTP(GMAIL_USER, GMAIL_PASS)
        yag.send(to=recipient_email, subject=subject, contents=body, attachments=attachment_path)
        print(f"💌 Wedding invite sent to {recipient_email}!")
    except Exception as e:
        print(f"❌ Error: {e}")

# === Main - Send the email ===
recipient = "ldumbatsuro6@gmail.com"  # Change to the recipient's email
subject = "You're Invited! Bani & Jay's Wedding 💕"
body = "Dear Guest,\n\nYou’re warmly invited to celebrate the wedding of Bani & Jay. Please find your invitation attached.\n\nLooking forward to seeing you there!\n\nWith love,\nThe Couple"
attachment_path = "bani_jay_wedding_invite.png"  # Path to your invitation image

# Send the email
send_wedding_invite(recipient, subject, body, attachment_path) 
