# receiptd
This is a simple service that can be used with a physical receipt printer

For more info, see my blog article: TODO

## Using `print.py`

## Using `print_server.py`
This is a tiny Flask app that enables printing over the local network. You can launch it like this:

```bash
gunicorn -w 4 -b 0.0.0.0:4020 'print_server:app'
```

Then, you can invoke a print job as follows:

```bash
curl 'http://localhost:4020/print/job?name=test&status=ok&hostname=hostname'
```

If you have a machine on, say, `serpent.local` then you can query `http://serpent.local` and print receipts
over the network :)

## Licence
ISC licence
