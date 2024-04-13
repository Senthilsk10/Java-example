package com.rest.restapi;

import org.glassfish.jersey.server.ResourceConfig;
import org.springframework.stereotype.Component;

@Component
public class JerseyConfig extends ResourceConfig {
    public JerseyConfig() {
        //register(MathController.class);
        register(FormController.class);
    }
}
