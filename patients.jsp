<%@ page import="java.util.*" %>
<%@ page session="false" %>
<!DOCTYPE html>
<html>
<head><title>Patients</title></head>
<body>
<h1>Patients</h1>

<form action="PatientServlet" method="post">
  Name: <input type="text" name="name" required>
  <button type="submit">Add Patient</button>
</form>

<h2>Patient List</h2>
<ul>
<%
    List<String> patients = (List<String>)request.getAttribute("patients");
    if(patients != null){
        for(String p : patients){
            out.println("<li>" + p + "</li>");
        }
    }
%>
</ul>

<a href="index.jsp">Home</a>
</body>
</html>
