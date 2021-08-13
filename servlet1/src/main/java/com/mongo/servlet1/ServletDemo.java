package com.mongo.servlet1;

import java.io.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;

@WebServlet("/ser1")
public class ServletDemo extends HttpServlet {
//    private String message;
    String data;

    public void init() {
        this.data = new MongoConn().getData();
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html; charset=UTF-8");
        response.setHeader("Conten-type", "text/html; charset=UTF-8");
        // Hello
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<body>");
        out.println("<meta charset='utf-8'/>");
        out.println("<h1>" + this.data + "</h1>");
        out.println("</body>");
        out.println("</html>");
    }

    public void destroy() {
    }
}