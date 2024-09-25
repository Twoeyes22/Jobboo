function loadTeam(teamId) {
    window.location.href = `/team/${teamId}`;
}

// 유저 카드 열기
function openModal(userId) {

    let selectedUserId = userId

    // API 호출
    fetch(`/api/user/${userId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error! status: ${response.status}");
            }
            return response.json();
        })
        .then(data => {
            if (data && data.u_id) {
                // 데이터를 모달에 채워넣기
                document.getElementById('user-name').innerText = data.u_name;
                document.getElementById('user-nickname').innerText = data.u_nickname;
                document.getElementById('user-email').innerText = data.u_email;
                document.getElementById('user-git').innerText = data.u_git;
                
                // 모달 표시
                document.getElementById('userModal').style.display = "block";

                // 삭제 버튼에 user-id를 파라미터로 넘기도록 설정
                const deleteButton = document.getElementById('delete-button');
                deleteButton.setAttribute('onclick', `openDeleteUserModal(${data.u_id})`);
                
            } else {
                console.log("data 속성이 존재하지 않음")
            }
        })
        .catch(error => {
            console.error('Error fetching user info:', error);
            alert('Failed to load user info.', );
        });
}

// 유저 카드 닫기
function closeModal() {
    document.getElementById('userModal').style.display = "none";
}

// 팀 삭제 모달 열기
function openDeleteTeamModal(teamId) {

    selectedTeamId = teamId;

    // API를 통해 팀 이름을 가져와 모달에 표시 (필요 시)
    fetch(`/current_team/${teamId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error! status: ${response.status}");
            }
            return response.json();
        })
        .then(data => {
            if (data && data.t_name) {
                //팀 이름을 모달에 표시
                document.getElementById('modal-team-name').innerText = data.t_name;
                document.getElementById('deleteForm').action = `/team/delete/${data.t_id}`; // 폼의 action을 설정
                // 모달 표시
                document.getElementById('deleteModal').style.display = "block";
                
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


// 유저 삭제 모달 열기
function openDeleteUserModal(userId) {

    selectedUserId = userId;

    // API를 통해 유저 이름을 가져와 모달에 표시 (필요 시)
    fetch(`/api/user/${userId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error! status: ${response.status}");
            }
            return response.json();
        })
        .then(data => {
            if (data && data.u_name) {
                //팀 이름을 모달에 표시
                document.getElementById('modal-user-name').innerText = data.u_name;
                document.getElementById('deleteUserForm').action = `/user/delete/${data.u_id}`; // 폼의 action을 설정
                // 모달 표시
                document.getElementById('deleteUserModal').style.display = "block";
                
            } else {
                console.log("data.u_name 속성이 존재하지 않음",data.u_name)   
            }}
        )
        .catch(error => {
            console.log("ERROR: ",error)
            alert('Failed to load user info.');
        });
}
// 유저 삭제 모달 닫기
function closeUserDeleteModal() {
    document.getElementById('deleteUserModal').style.display = "none";
}
// 모달 외부를 클릭하면 모달 닫기
window.onclick = function(event) {
    const modal = document.getElementById('deleteUserModal');
    if (event.target === modal) {
        modal.style.display = "none";
    }
};