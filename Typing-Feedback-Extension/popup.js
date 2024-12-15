document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.getElementById('toggleButton');

  // 초기 상태 로드
  chrome.storage.local.get('extensionActive', (result) => {
    const isActive = result.extensionActive || false;
    toggleButton.style.backgroundColor = isActive ? 'green' : 'red';
    toggleButton.textContent = isActive ? 'Active' : 'Inactive';
  });

  // 버튼 클릭 이벤트
  toggleButton.addEventListener('click', () => {
    chrome.storage.local.get('extensionActive', (result) => {
      const newState = !result.extensionActive;
      chrome.storage.local.set({ extensionActive: newState });

      // 버튼 상태 업데이트
      toggleButton.style.backgroundColor = newState ? 'green' : 'red';
      toggleButton.textContent = newState ? 'Active' : 'Inactive';
    });
  });
});
