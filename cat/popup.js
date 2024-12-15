document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.getElementById('toggleButton');
  const imageUrlInput = document.getElementById('imageUrl');
  const imageSizeSlider = document.getElementById('imageSizeSlider');
  const speedSlider = document.getElementById('speedSlider');

  // 초기 상태 로드
  chrome.storage.local.get(['imageActive', 'imageUrl', 'imageSize', 'speed'], (result) => {
    toggleButton.textContent = result.imageActive ? 'Deactivate' : 'Activate';
    imageUrlInput.value = result.imageUrl || '';
    imageSizeSlider.value = result.imageSize || 150;
    speedSlider.value = result.speed || 10;
  });

  // 이미지 URL 저장
  imageUrlInput.addEventListener('input', () => {
    chrome.storage.local.set({ imageUrl: imageUrlInput.value });
  });

  // 이미지 크기 저장
  imageSizeSlider.addEventListener('input', () => {
    chrome.storage.local.set({ imageSize: imageSizeSlider.value });
  });

  // 속도 저장
  speedSlider.addEventListener('input', () => {
    chrome.storage.local.set({ speed: speedSlider.value });
  });

  // 버튼 클릭 이벤트
  toggleButton.addEventListener('click', () => {
    chrome.storage.local.get('imageActive', (result) => {
      const newState = !result.imageActive;
      chrome.storage.local.set({ imageActive: newState });
      toggleButton.textContent = newState ? 'Deactivate' : 'Activate';
    });
  });
});
