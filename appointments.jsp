<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>
<head><title>Appointments</title></head>
<body>
<h1>Appointments</h1>

<form action="AppointmentServlet" method="post">
  Patient Name: <input type="text" name="patient" required>
  Date: <input type="date" name="date" required>
  <button type="submit">Book Appointment</button>
</form>

<h2>Appointment List</h2>
<ul>
<%
    List<String> appointments = (List<String>)request.getAttribute("appointments");
    if(appointments != null){
        for(String a : appointments){
            out.println("<li>" + a + "</li>");
        }
    }
%>
</ul>

<a href="index.jsp">Home</a>
</body>
</html>
