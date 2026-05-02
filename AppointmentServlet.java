package com.healthcare;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.util.*;

public class AppointmentServlet extends HttpServlet {
    private static List<String> appointments = new ArrayList<>();

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setAttribute("appointments", appointments);
        RequestDispatcher rd = request.getRequestDispatcher("appointments.jsp");
        rd.forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String patient = request.getParameter("patient");
        String date = request.getParameter("date");
        if (patient != null && date != null) {
            appointments.add("Patient: " + patient + " | Date: " + date);
        }
        response.sendRedirect("appointments.jsp");
    }
}
