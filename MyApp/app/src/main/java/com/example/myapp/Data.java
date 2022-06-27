package com.example.myapp;

public class Data {

    private String time;
    private String val;
    private String Humidity;
    private String Temperature;
    private String detection;


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }

    public String getHumidity() {
        return Humidity;
    }

    public void setHumidity(String humidity) {
        Humidity = humidity;
    }

    public String getTemperature() {
        return Temperature;
    }

    public void setTemperature(String temperature) {
        Temperature = temperature;
    }

    public String getDetection() {
        return detection;
    }

    public void setDetection(String detection) {
        this.detection = detection;
    }

    public Data(String time, String val, String humidity, String temperature, String detection) {
        this.time = time;
        this.val = val;
        this.Humidity = humidity;
        this.Temperature = temperature;
        this.detection = detection;
    }


    public Data() {
    }


}
