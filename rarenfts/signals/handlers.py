from __future__ import print_function
import os
from django.dispatch import receiver
from rarenfts.models import Collection
from django.contrib.auth import get_user_model
from decouple import config
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from rarenfts.signals import alert_admin_signal

@receiver(alert_admin_signal)
def alert_admin(**kwargs):
    instance = kwargs['instance']
    if kwargs['created'] :
        admin_emails = get_user_model().objects.filter(is_staff=True).values()

        if admin_emails:

            configuration = sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = os.environ.get('API_KEY')

            api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
                sib_api_v3_sdk.ApiClient(configuration))
            sender = {"name": "Admin", "email": "nftlookout5@gmail.com"}
            subject = None
            html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
            to = list(admin_emails)
            params = {"name": instance.name, "network": instance.network}

            send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
                to=to, html_content=html_content, sender=sender, subject=subject,  template_id=2, params=params)

            try:
                api_response = api_instance.send_transac_email(send_smtp_email)
                print(api_response)
            except ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


