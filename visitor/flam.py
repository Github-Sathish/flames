name1='ANKIT'
name2='DEEPIKA'
name1.replace(" ",'')
name2.replace(" ",'')
name1.lower()
name2.lower()
name1 = list(name1)
name2 = list(name2)

flames = ['f','l','a','m','e','s']
for i in name1:
    for j in name2:
        if i==j:
            name1.remove(i)
            name2.remove(j)
name3 = name1+name2
print(name3)
# uniq_ct = len(name3)
        

count = len(name1) + len(name2)
 
# list of FLAMES acronym
result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

# keep looping until only one item
# is not remaining in the result list
while len(result) > 1:

    # store that index value from
    # where we have to perform slicing.
    split_index = (count % len(result) - 1)

    # this steps is done for performing
    # anticlock-wise circular fashion counting.
    if split_index >= 0:

        # list slicing
        right = result[split_index + 1:]
        left = result[: split_index]

        # list concatenation
        result = right + left

    else:
        result = result[: len(result) - 1]

# print final result
print("Relationship status :", result[0])





# while(len(flames)>1):
#     print(count,len(flames))
#     # q = count // len(flames)
#     s = s*10
#     print(count,'============',s)
#     letter = s[count-1]
#     flames.remove(letter)
#     s = "".join(flames)
#     print(s)

# result = flames[0]






# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>FLAMES Game</title>
#     <link rel="stylesheet" href="{% static 'your_app/styles.css' %}">
# </head>
# <body>
#     <h1>FLAMES Game</h1>
    
#     <form id="flamesForm">
#         {% csrf_token %}
#         <!-- Include CSRF token in the form -->
        
#         <label for="yourName">Your Name:</label>
#         <input type="text" id="yourName" required>

#         <label for="partnerName">Partner's Name:</label>
#         <input type="text" id="partnerName" required>

#         <button type="button" onclick="submitForm()">Submit</button>
#     </form>

#     <div id="result"></div>

#     <script>
#         // ... (Your JavaScript code remains unchanged)
#         function submitForm() {
#             var yourName = document.getElementById('yourName').value;
#             var partnerName = document.getElementById('partnerName').value;
            
#             // Get CSRF token from cookies
#             var csrftoken = getCookie('csrftoken');

#             fetch('/visitor/getResult/', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json',
#                     'X-CSRFToken': csrftoken,
#                 },
#                 body: JSON.stringify({
#                     your_name: yourName,
#                     partner_name: partnerName,
#                 }),
#             })
#             .then(response => response.json())
#             .then(data => {
#                 // Display the result
#                 document.getElementById('result').innerHTML = 'Relationship Status: ' + data.message;
#             })
#             .catch(error => console.error('Error:', error));
#         }

#         // Function to get CSRF token from cookies
#         function getCookie(name) {
#             var cookieValue = null;
#             if (document.cookie && document.cookie !== '') {
#                 var cookies = document.cookie.split(';');
#                 for (var i = 0; i < cookies.length; i++) {
#                     var cookie = cookies[i].trim();
#                     if (cookie.substring(0, name.length + 1) === (name + '=')) {
#                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
#                         break;
#                     }
#                 }
#             }
#             return cookieValue;
#         }
#     </script>
# </body>
# </html>
