import urllib.parse
query = 'Corner Guys'
print(urllib.parse.quote(query))

  <script>
    function autoEncode() {
      var inputs = document.querySelectorAll('input');
      for (var i = 0; i < inputs.length; i++) {
        inputs[i].value = encodeURIComponent(inputs[i].value);
      }
    }
  
    document.addEventListener('submit', autoEncode);
  </script>