class Notification:
    def send_message(self, message):
        raise NotImplementedError("Subclasses must implement send_message()")


class EmailNotification(Notification):
    def send_message(self, message):
        subject = "School Update"
        print("Sending Email...")
        print("Subject:", subject)
        print("Message:", message)
        print("Email sent successfully.\n")


class SMSNotification(Notification):
    def send_message(self, message):
        # Simulating SMS character limit
        if len(message) > 50:
            message = message[:50] + "..."
        print("Sending SMS...")
        print("Message:", message)
        print("SMS sent successfully.\n")


class AppNotification(Notification):
    def send_message(self, message):
        print("Sending App Notification...")
        print("Push Alert:", message)
        print("Stored in notification center.")
        print("App notification sent successfully.\n")


def notify(notification_method, message):
    notification_method.send_message(message)


email = EmailNotification()
sms = SMSNotification()
app = AppNotification()

message_text = "Tomorrow is a holiday due to heavy rain. Stay safe."

notify(email, message_text)
notify(sms, message_text)
notify(app, message_text)
