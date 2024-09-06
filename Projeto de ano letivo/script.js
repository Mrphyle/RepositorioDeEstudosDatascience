function openGoogle() {
  // Obtem as dimensões da tela
  var screenWidth = window.innerWidth;
  var screenHeight = window.innerHeight;

  // Define o tamanho do pop-up como 80% da largura e altura da tela, com um tamanho mínimo
  var popupWidth = Math.max(screenWidth * 0.8, 300); // No mínimo 300px de largura
  var popupHeight = Math.max(screenHeight * 0.8, 300); // No mínimo 300px de altura

  window.open("https://www.google.com", "popup", "width=" + popupWidth + ",height=" + popupHeight);
}