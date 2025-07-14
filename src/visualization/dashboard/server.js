const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Cost Optimization Dashboard');
});

app.listen(PORT, () => {
  console.log(`Dashboard server running on port ${PORT}`);
});
