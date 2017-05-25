Notes 2015_08_24

To change the django settings form local to testing:
```bash
python manage.py shell --settings=payment2.settings.testing
from django.conf import settings
dir(settings)
```

To connect 30 server:
```bash
ssh python@192.168.100.30
```

Manually doing reconcliations
```bash
from wechatpay.wechatpay import DownloadBill as WeChatDownloadBill
WeChatDownloadBill().get_bill('2015-08-21')

from jdpay.jdpay import DownloadBill as JDDownloadBill
JDDownloadBill().get_bill(bill_date='2015-08-21', suffix='_0430')

from reconciliations import reconciliations
reconciliations.WCRecon('2015-08-21').write_to_recon()
reconciliations.JDRecon('2015-08-21').write_to_recon()
```