package com.crud.cruddemo;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
//import java.util.List;


@RestController
@RequestMapping("/users")
public class UserModelController {

    @Autowired
    private UserModelRepository UserModelRepository;

    @GetMapping("/")
    public java.util.List<UserModel> getAllUserModels() {
        return UserModelRepository.findAll();
    }

    @PostMapping("/")
    public UserModel createUserModel(@RequestBody UserModel UserModel) {
        return UserModelRepository.save(UserModel);
    }

    @GetMapping("/{id}")
    public UserModel getUserModelById(@PathVariable Integer id) {
        return UserModelRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("UserModel not found with id: " + id));
    }

    @PutMapping("/{id}")
    public UserModel updateUserModel(@PathVariable Integer id, @RequestBody UserModel UserModelDetails) {
        UserModel UserModel = UserModelRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("UserModel not found with id: " + id));

        UserModel.setFirstName(UserModelDetails.getFirstName());
        UserModel.setLastName(UserModelDetails.getLastName());
        UserModel.setEmail(UserModelDetails.getEmail());

        return UserModelRepository.save(UserModel);
    }

    @DeleteMapping("/{id}")
    public void deleteUserModel(@PathVariable Integer id) {
        UserModelRepository.deleteById(id);
    }
}
