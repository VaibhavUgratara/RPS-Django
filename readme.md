<h1>ROCK PAPER SCISSORS</h1>

A simple multiplayer Rock Paper Scissors game built using Django
<br>
<ul>
<li>Create a room and share the Room ID with your opponent</li>
<li>The opponent joins the room by entering the shared Room ID</li>
<li>Now you're good to go!! Play Rock Paper Scissors from anywhere</li>
</ul>
<br>
<h2>Key Concepts:</h2>
<ol>
<li>Django</li>
<li>Jinja2</li>
<li>Websockets (Django Channels)</li>
</ol>

<h5>Points to remember</h5>
<ul>
<li>I am still figuring out how can I host the project as i am facing some difficulties.</li>
<li>To run this project all devices must be connected to the same network as the server.</li>
</ul>

<h5>How to run the project?</h1>
<ul>
<li><p>First install all packges by running this command:</p>
<pre>pip install -r requirements.txt</pre>
</li>
<li><p>Now locate the <strong>manage.py</strong> file and run the following commands:</p>
<pre>python manage.py makemigrations</pre>
<pre>python manage.py migrate</pre>
</li>
<li>Now connect the other devices and host (server) with the same network</li>
<li>Now run this command:</p>
<pre>python manage.py runserver 0.0.0.0:[port_number]</pre>
</li>
<li><p>Now get the IP address of the host device(server) and in the other devices go to the URL:</p>
<pre>http://[server_IP_address]:[port_number]</pre>
</ul>

<h6>e.g.</h6>
<ol>
<li>Run command : python manage.py runserver 0.0.0.0:8000</li>
<li>Let's assume the server IP address is : 192.16x.x.x</li>
<li>The URL will be: http://192.16x.x.x:8000</li>
</ol>