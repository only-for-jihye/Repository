import React, { useEffect, useState } from 'react';
import axios from 'axios';


function UserList() {
    const [users, setUsers] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchUsers = async () => {
        try {
            setUsers(null);
            setError(null);
            setLoading(true);
            const response = await axios.get('http://localhost:3000/users/');
            setUsers(response.data);
            console.log(response.data);
        } catch (e) {
            setError(e);
        }
        setLoading(false);
    };

    useEffect( () => {
        fetchUsers();
    },[])

    if (loading) return <div>Loading...</div>
    if (error) return <div>Error...</div>
    if (!users) return null;

    return (
        <>
            <ul>
                {users.map(user => <li key={user.id}>
                    {user.id} {user.name} {user.age} [{user.married ? '기혼' : '미혼'}] ({user.created_at})
                </li>)}
            </ul>
            <button onClick={fetchUsers}>reloading...</button>
        </>
    );

}

export default UserList;