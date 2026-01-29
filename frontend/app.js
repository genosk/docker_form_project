const express = require("express");
const path = require("path");

const app = express();

// Serve static files (index.html)
app.use(express.static(__dirname));

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});
    
