var express = require("express");
var router = express.Router();
require("dotenv").config();
const axios = require("axios");
const background = process.env.BACKGROUND_COLOR;

const api = axios.create({
  // baseURL: "https://backend.icywater-2b0d0fc0.japaneast.azurecontainerapps.io",
  baseURL: process.env.API_BASE_URL,
  params: {},
  timeout: process.env.TIMEOUT || 15000,
});

/* GET home page. */
router.get("/", async function (req, res, next) {
  try {
    console.log("Sending request to backend menus api");
    var data = await api.get("/menus");
    console.log("Response from backend menus api: ", data.data);

    // filter the response json list to only include the menu items whose category is "Chinese"
    data.data = data.data.filter((item) => item.category === "Chinese");


    res.render("index", {
      menus: data.data,
      background_color: background,
    });
  } catch (err) {
    console.log("Error: ", err);
    next(err);
  }
});

module.exports = router;
