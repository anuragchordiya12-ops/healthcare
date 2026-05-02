package com.healthcare;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.util.*;

public class PatientServlet extends HttpServlet {
    private static List<String> patients = new ArrayList<>();

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setAttribute("patients", patients);
        RequestDispatcher rd = request.getRequestDispatcher("patients.jsp");
        rd.forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String name = request.getParameter("name");
        if (name != null && !name.isEmpty()) {
            patients.add(name);
        }
        response.sendRedirect("patients.jsp");
    }
}
