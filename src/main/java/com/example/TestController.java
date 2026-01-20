@RestController
public class TestController {
    @GetMapping("/user/{id}")
    public User getUser(@PathVariable Long id) {
        return userRepository.findById(id).get(); 
    }
}
