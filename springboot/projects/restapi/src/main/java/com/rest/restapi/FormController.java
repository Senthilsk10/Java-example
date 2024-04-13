package com.rest.restapi;

import org.springframework.stereotype.Component;

import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.FormParam;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.core.MediaType;

@Component
@Path("/submit")
public class FormController {

    @POST
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public void submitForm(@FormParam("username") String username,
                           @FormParam("password") String password) {
        // Process the form data
        System.out.println("Received Form Data - Username: " + username + ", Password: " + password);
        // You can perform further processing, validations, and database operations here
    }
}

