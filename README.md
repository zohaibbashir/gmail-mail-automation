# gmail-mail-automation
A Python script that is used to automate sending emails
### Command Line Options

- `-e`: Sender's email address.
- `-p`: Password for the sender's email address. If not provided, the script will prompt for it securely.
- `-to`: Recipient's email address.
- `-cc`: CC email address.
- `-bcc`: BCC email address.
- `-S`: Email subject.
- `-T`: Email text or body.

### Example Usage

```bash
python a.py -e sender@example.com -p password123 -to recipient@example.com -S "Subject" -T "Hello, this is the email body."
