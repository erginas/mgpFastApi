// UserModal.jsx
import React from "react";
import GenericFormModal from "../forms/GenericFormModal";

const UserModal = ({ isOpen, onClose, onSubmit, initialData }) => {
    return (
        <GenericFormModal
            isOpen={isOpen}
            onClose={onClose}
            onSubmit={onSubmit}
            initialData={initialData}
            initialValues={initialData}
        />
    );
};

export default UserModal;