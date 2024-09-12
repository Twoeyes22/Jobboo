function loadTeam(teamId) {
    window.location.href = `/team/${teamId}`;
}

// 유저 카드 열기
function openModal(userId) {
    // API 호출
    fetch(`/user/${userId}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                // 데이터를 모달에 채워넣기
                document.getElementById('user-name').innerText = data.u_name;
                document.getElementById('user-nickname').innerText = data.u_nickname;
                document.getElementById('user-email').innerText = data.u_email;
                document.getElementById('user-git').innerText = data.u_git;
                
                // 모달 표시
                document.getElementById('userModal').style.display = "block";
            }
        })
        .catch(error => {
            console.error('Error fetching user info:', error);
            alert('Failed to load user info.');
        });
}

// 유저 카드 닫기
function closeModal() {
    document.getElementById('userModal').style.display = "none";
}