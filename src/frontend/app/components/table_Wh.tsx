import React, { useState } from 'react';
import styles from '../styles/Table.module.css';

const Table = ({ data }) => {
    const [selectedRow, setSelectedRow] = useState<number | null>(null);

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
                {data.map((item, index) => (
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
