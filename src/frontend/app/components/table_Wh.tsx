import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from '../styles/Table.module.css';

const Table = () => {
    const [tableData, setTableData] = useState([]);
    const [selectedRow, setSelectedRow] = useState<number | null>(null);

    useEffect(() => {
        // Ao montar o componente, fazer a requisição GET para obter dados da tabela
        axios.get('http://127.0.0.1:8000/warehouse')
            .then(response => setTableData(response.data))
            .catch(error => console.error('Erro ao obter dados da tabela:', error));
    }, []);

    return (
        <table className={styles.tabela}>
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Status</th>
                    <th>Quantidade</th>
                </tr>
            </thead>
            <tbody>
                {tableData.map((item, index) => (
                    <tr
                        key={index}
                        className={selectedRow === index ? styles.selectedRow : ""}
                        onClick={() => setSelectedRow(index)}
                    >
                        <td>{item.Name}</td>
                        <td>{item.Status ? 'Contém' : 'Esgotado'}</td>
                        <td>{item.Amout}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default Table;