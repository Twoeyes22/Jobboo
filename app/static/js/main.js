function loadTeam(teamId) {
    window.location.href = `/team/${teamId}`;
}

// 유저 카드 열기
function openModal(userId) {
    // API 호출
    fetch(`/api/user/${userId}`)
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

// 팀 삭제 모달 열기
function openDeleteModal(teamId) {

    selectedTeamId = teamId;

    // API를 통해 팀 이름을 가져와 모달에 표시 (필요 시)
    fetch(`/current_team/${teamId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error! status: ${response.status}");
            }
            return response.json();
        })
        //.then(response => console.log("response:",response))
        //.then(response => console.log("name: ", response.t_name, "id: ", response.t_id))
        .then(data => {
            console.log("data:",data)
            if (data && data.t_name) {
                //팀 이름을 모달에 표시
                document.getElementById('modal-team-name').innerText = data.t_name;
                document.getElementById('deleteForm').action = `/team/delete/${data.t_id}`; // 폼의 action을 설정
                // 모달 표시
                document.getElementById('deleteModal').style.display = "block";
                console.log("no error")
            } else {
                console.log("data.t_name 속성이 존재하지 않음",data.t_name)   
            }}
        )
        .catch(error => {
            console.log("ERROR: ",error)
            alert('Failed to load team info.');
        });
}

// 팀 삭제 모달 닫기
function closeDeleteModal() {
    document.getElementById('deleteModal').style.display = "none";
}

// 모달 외부를 클릭하면 모달 닫기
window.onclick = function(event) {
    const modal = document.getElementById('deleteModal');
    if (event.target === modal) {
        modal.style.display = "none";
    }
};