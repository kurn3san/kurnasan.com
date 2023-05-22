const translations = {
    en: {
      welcomeTitle: "Welcome",
      welcomeMessage: "This is the welcoming message.",
    },
    fr: {
      welcomeTitle: "Bienvenue",
      welcomeMessage: "Ceci est le message de bienvenue.",
    },
    // Add more translations for other languages
  };
  
  function changeLanguage(language) {
    const selectedLanguage = translations[language];
    if (selectedLanguage) {
      document.getElementById("welcome-title").textContent = selectedLanguage.welcomeTitle;
      document.getElementById("welcome-message").textContent = selectedLanguage.welcomeMessage;
      // Update other text content as needed
    }
  }
  