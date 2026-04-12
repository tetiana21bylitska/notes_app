import telebot
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Note

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)


@receiver(post_save, sender=Note)
def send_new_note_to_tg(sender, instance, created, **_kwargs):

    if created and not instance.remind_at:
        try:
            message = (
                f"<b>Нова нотатка: {instance.title}</b>\n\n"
                f"{instance.text}"
            )
            bot.send_message(
                settings.TELEGRAM_CHANNEL_ID,
                message,
                parse_mode='HTML'
            )
            Note.objects.filter(pk=instance.pk).update(is_sent=True)
        except Exception as e:
            print(f"DEBUG: Помилка ТГ: {e}")