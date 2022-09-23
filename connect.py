#     BARCODE GENERATOR
  # make sure you have installed Python, [Pillow], [Scratchattach], [qrcode]
  # make sure both files are at the same folder!
import scratchattach as scratch3
import generator

session = scratch3.login("YOUR USERNAME HERE", "YOUR PASSWORD HERE")
conn = session.connect_cloud(project_id="PROJECT ID")

client = scratch3.CloudRequests(conn)

@client.request
def checkcon(): 
    return "success"
@client.request
def encode(argument1):
    return generator.gen_qr(argument1)

@client.event
def on_ready():
    print("Request handler is running")

client.run()
