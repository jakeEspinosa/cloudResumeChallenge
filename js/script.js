const URL = "https://api.jakeespinosa.com/visitorcount"
const httpRequest = new XMLHttpRequest();

function handler() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
            response = httpRequest.responseText;
            let responseObj = JSON.parse(response);
            let text = responseObj['visitorCount']
            
            const para = document.createElement('p');
            const node = document.createTextNode("Visitor Count: " + text);
            para.appendChild(node);
            const element = document.getElementById("div1");
            element.appendChild(para);

          } else {
            alert("There was a problem with the request.");
          }
        }
    }
  
httpRequest.onreadystatechange = handler;

httpRequest.open("GET", URL);
httpRequest.send();