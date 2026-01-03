package com.guildly.tck.controller;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;
import java.util.Map;

@Controller
public class TckController {

    private final ObjectMapper mapper = new ObjectMapper();

    // HTML site
    @GetMapping("/")
    public String index(Model model) throws IOException {
        List<Map<String, Object>> maddeler = mapper.readValue(
                new ClassPathResource("data/maddeler.json").getFile(),
                new TypeReference<List<Map<String, Object>>>(){}
        );
        model.addAttribute("maddeler", maddeler);
        return "index";
    }

    // API: tüm maddeler
    @GetMapping("/api/maddeler")
    @ResponseBody
    public List<Map<String, Object>> getMaddeler() throws IOException {
        return mapper.readValue(
                new ClassPathResource("data/maddeler.json").getFile(),
                new TypeReference<List<Map<String, Object>>>(){}
        );
    }

    // API: madde no ile
    @GetMapping("/api/maddeler/{madde_no}")
    @ResponseBody
    public Map<String, Object> getMadde(@PathVariable int madde_no) throws IOException {
        List<Map<String, Object>> maddeler = mapper.readValue(
                new ClassPathResource("data/maddeler.json").getFile(),
                new TypeReference<List<Map<String, Object>>>(){}
        );
        return maddeler.stream()
                .filter(m -> (Integer)m.get("madde_no") == madde_no)
                .findFirst()
                .orElse(Map.of("detail", "Madde bulunamadı"));
    }

    // API: ceza
    @GetMapping("/api/cezalar/{madde_no}")
    @ResponseBody
    public Map<String, Object> getCeza(@PathVariable int madde_no) throws IOException {
        List<Map<String, Object>> cezalar = mapper.readValue(
                new ClassPathResource("data/cezalar.json").getFile(),
                new TypeReference<List<Map<String, Object>>>(){}
        );
        return cezalar.stream()
                .filter(c -> (Integer)c.get("madde_no") == madde_no)
                .findFirst()
                .orElse(Map.of("detail", "Ceza bilgisi yok"));
    }
}
