#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html>"
echo "<head>"
echo "<title>Bash as CGI</title>"
echo "</head>"
echo "<style>"
echo "p{
      color: navy; 
      max-width: 500px; 
      text-indent: 30px;
      }
      pre {
          width=100%; 
          border: 1px solid black; 
          display: table; 
          border-collapse: separate;
          }"
echo "</style>"

echo "<body>"
echo "<h3>Port Scan Results</h3>"
site=`echo "$QUERY_STRING" | sed 's/site=//'`
 "<pre><p>"
echo "SCANNING "$site"...."
echo $(nmap -p21-23,80,110,143,443,3389 $site)
echo "<br><br><a href="test.html">NEW SCAN</a>"
echo "<p></pre>"
echo "</body></html>"

