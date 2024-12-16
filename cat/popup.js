document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.getElementById('toggleButton');
  const imageUrlInput = document.getElementById('imageUrl');
  const imageSizeSlider = document.getElementById('imageSizeSlider');
  const speedSlider = document.getElementById('speedSlider');

  // Load initial state
  chrome.storage.local.get(['imageActive', 'imageUrl', 'imageSize', 'speed'], (result) => {
    toggleButton.textContent = result.imageActive ? 'Deactivate' : 'Activate';
    imageUrlInput.value = result.imageUrl || '';
    imageSizeSlider.value = result.imageSize || 150;
    speedSlider.value = result.speed || 10;
  });

  // Save image URL
  imageUrlInput.addEventListener('input', () => {
    chrome.storage.local.set({ imageUrl: imageUrlInput.value });
  });

  // Save image size
  imageSizeSlider.addEventListener('input', () => {
    chrome.storage.local.set({ imageSize: imageSizeSlider.value });
  });

  // Save speed
  speedSlider.addEventListener('input', () => {
    chrome.storage.local.set({ speed: speedSlider.value });
  });

  // Toggle button action
  toggleButton.addEventListener('click', () => {
    chrome.storage.local.get('imageActive', (result) => {
      const newState = !result.imageActive;
      chrome.storage.local.set({ imageActive: newState });
      toggleButton.textContent = newState ? 'Deactivate' : 'Activate';
    });
  });
});
