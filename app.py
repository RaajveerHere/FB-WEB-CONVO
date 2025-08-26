from flask import Flask, request, render_template, redirect, url_for
import os
import time
import requests

app = Flask(__name__)

# Static variables for headers
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
}

@app.route('/')
def index():
    return '''
    <div id='content'>
<!-- info --><div style="font-size: 20px">
<script type="text/javascript">
farbbibliothek = new Array();
farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100");
farbbibliothek[1] = new Array("#00FF00","#000000","#00FF00","#00FF00");
farbbibliothek[2] = new Array("#00FF00","#FF0000","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00");
farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040");
farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000");
farbbibliothek[5] = new Array("#000000","#000000","#000000","#FFFFFF","#FFFFFF","#FFFFFF");
farbbibliothek[6] = new Array("#0000FF","#FFFF00");
farben = farbbibliothek[4];
function farbschrift(){for(var b=0;b<Buchstabe.length;b++){document.all["a"+b].style.color=farben[b]}farbverlauf()}function string2array(b){Buchstabe=new Array();while(farben.length<b.length){farben=farben.concat(farben)}k=0;while(k<=b.length){Buchstabe[k]=b.charAt(k);k++}}function divserzeugen(){for(var b=0;b<Buchstabe.length;b++){document.write("<span id='a"+b+"' class='a"+b+"'>"+Buchstabe[b]+"</span>")}farbschrift()}var a=1;function farbverlauf(){for(var b=0;b<farben.length;b++){farben[b-1]=farben[b]}farben[farben.length-1]=farben[-1];setTimeout("farbschrift()",30)}var farbsatz=1;function farbtauscher(){farben=farbbibliothek[farbsatz];while(farben.length<text.length){farben=farben.concat(farben)}farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001))}setInterval("farbtauscher()",5000);
 
text= "💙💚❤️THIS WEB PAGE IS MADE BY Mr.RAAJVEER BOSS 💫💯🟥🟨🟧OWNER :- Mr.RAAJVEER BOSS ✨🍁🌹"; //h
string2array(text);
divserzeugen();
//document.write(text);
</script></div>
<p id='name'>           
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>RAAJVEER BOSS ❤️</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
          <style>
            body {
              background-color: white;
            }
            .container {
              max-width: 370px;
              background-color: yellow;
              border-radius: 10px;
              padding: 20px;
              box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
              margin: 0 auto;
              margin-top: 20px;
            }
            .header {
              text-align: center;
              padding-bottom: 10px;
            }
            .btn-submit {
              width: 100%;
              margin-top: 10px;
            }
            .footer {
              text-align: center;
              margin-top: 10px;
              color: blue;
            }
          </style>
        </head>
        <body>
          <header class="header mt-4">
            <h1 class="mb-3">🚀 RAAJVEER BOSS✨</h1>
            <h3>OWNER BY MR. RAAJVEER BOSS ❤️</h3>
          </header>

          <div class="container">
            <form action="/" method="post" enctype="multipart/form-data">
              <div class="mb-3">
                <label for="tokenType">Select Token Type:</label>
                <select class="form-control" id="tokenType" name="tokenType" required>
                  <option value="single">Single Token</option>
                  <option value="multi">Multi Token</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="accessToken">Enter Your Token:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken">
              </div>
              <div class="mb-3">
                <label for="threadId">Enter Convo/Inbox ID:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
              </div>
              <div class="mb-3">
                <label for="kidx">Enter Hater Name:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
              </div>
              <div class="mb-3">
                <label for="txtFile">Select Your Notepad File:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
              </div>
              <div class="mb-3" id="multiTokenFile" style="display: none;">
                <label for="tokenFile">Select Token File (for multi-token):</label>
                <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
              </div>
              <div class="mb-3">
                <label for="time">Speed in Seconds:</label>
                <input type="number" class="form-control" id="time" name="time" required>
              </div>
              <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
            </form>
          </div>
          <footer class="footer">
            <p>&copy; Developed by RAAJVEER BOSS 2024. All Rights Reserved.</p>
            <p>Convo/Inbox Web Tool</p>
            <p>Keep Enjoying!</p>
          </footer>
        </body>
        </html>
    '''

@app.route('/', methods=['POST'])
def process_form():
    token_type = request.form.get('tokenType')
    access_token = request.form.get('accessToken')
    thread_id = request.form.get('threadId')
    hater_name = request.form.get('kidx')
    time_interval = int(request.form.get('time'))
    
    txt_file = request.files['txtFile']
    messages = txt_file.read().decode().splitlines()
    
    tokens = []
    if token_type == 'multi':
        token_file = request.files.get('tokenFile')
        if token_file:
            tokens = token_file.read().decode().splitlines()

    folder_name = f"Convo_{thread_id}"
    os.makedirs(folder_name, exist_ok=True)

    with open(os.path.join(folder_name, "details.txt"), "w") as f:
        f.write(f"Thread ID: {thread_id}\n")
        f.write(f"Hater Name: {hater_name}\n")
        f.write(f"Speed (s): {time_interval}\n")
        f.write("\n".join(messages))

    if tokens:
        with open(os.path.join(folder_name, "tokens.txt"), "w") as f:
            f.write("\n".join(tokens))

    post_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

    for message_index, message in enumerate(messages):
        token = access_token if token_type == 'single' else tokens[message_index % len(tokens)]
        data = {'access_token': token, 'message': f"{hater_name} {message}"}
        response = requests.post(post_url, json=data, headers=headers)

        if response.ok:
            print(f"[SUCCESS] Sent: {message}")
        else:
            print(f"[FAILURE] Failed to send: {message}")
        time.sleep(time_interval)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
