from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from notes.models import Note
import telebot


class Command(BaseCommand):
    help = 'Відправляє відкладені нотатки в Телеграм'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
        now = timezone.now()

        notes = Note.objects.filter(remind_at__lte=now, is_sent=False)

        for note in notes:
            message = f"Нагадування: {note.title}*\n\n{note.text}"
            try:
                bot.send_message(settings.TELEGRAM_CHANNEL_ID, message, parse_mode='Markdown')
                note.is_sent = True
                note.save()
                self.stdout.write(self.style.SUCCESS(f'Відправлено: {note.title}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Помилка: {e}'))