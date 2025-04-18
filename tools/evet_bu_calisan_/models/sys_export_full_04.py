from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SysExportFull04(Base):
    __tablename__ = 'sys_export_full_04'

    abort_step: Mapped[Optional[Integer]] = mapped_column(Integer)
    access_method: Mapped[Optional[String]] = mapped_column(String)
    ancestor_object_name: Mapped[Optional[String]] = mapped_column(String)
    ancestor_object_schema: Mapped[Optional[String]] = mapped_column(String)
    ancestor_object_type: Mapped[Optional[String]] = mapped_column(String)
    ancestor_process_order: Mapped[Optional[Integer]] = mapped_column(Integer)
    base_object_name: Mapped[Optional[String]] = mapped_column(String)
    base_object_schema: Mapped[Optional[String]] = mapped_column(String)
    base_object_type: Mapped[Optional[String]] = mapped_column(String)
    base_process_order: Mapped[Optional[Integer]] = mapped_column(Integer)
    block_size: Mapped[Optional[Integer]] = mapped_column(Integer)
    cluster_ok: Mapped[Optional[Integer]] = mapped_column(Integer)
    completed_bytes: Mapped[Optional[Integer]] = mapped_column(Integer)
    completed_rows: Mapped[Optional[Integer]] = mapped_column(Integer)
    completion_time: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    control_queue: Mapped[Optional[String]] = mapped_column(String)
    creation_level: Mapped[Optional[Integer]] = mapped_column(Integer)
    creation_time: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    cumulative_time: Mapped[Optional[Integer]] = mapped_column(Integer)
    data_buffer_size: Mapped[Optional[Integer]] = mapped_column(Integer)
    data_io: Mapped[Optional[Integer]] = mapped_column(Integer)
    dataobj_num: Mapped[Optional[Integer]] = mapped_column(Integer)
    db_version: Mapped[Optional[String]] = mapped_column(String)
    degree: Mapped[Optional[Integer]] = mapped_column(Integer)
    domain_process_order: Mapped[Optional[Integer]] = mapped_column(Integer)
    dump_allocation: Mapped[Optional[Integer]] = mapped_column(Integer)
    dump_fileid: Mapped[Optional[Integer]] = mapped_column(Integer)
    dump_length: Mapped[Optional[Integer]] = mapped_column(Integer)
    dump_orig_length: Mapped[Optional[Integer]] = mapped_column(Integer)
    dump_position: Mapped[Optional[Integer]] = mapped_column(Integer)
    duplicate: Mapped[Optional[Integer]] = mapped_column(Integer)
    elapsed_time: Mapped[Optional[Integer]] = mapped_column(Integer)
    error_count: Mapped[Optional[Integer]] = mapped_column(Integer)
    extend_size: Mapped[Optional[Integer]] = mapped_column(Integer)
    file_max_size: Mapped[Optional[Integer]] = mapped_column(Integer)
    file_name: Mapped[Optional[String]] = mapped_column(String)
    file_type: Mapped[Optional[Integer]] = mapped_column(Integer)
    flags: Mapped[Optional[Integer]] = mapped_column(Integer)
    grantor: Mapped[Optional[String]] = mapped_column(String)
    granules: Mapped[Optional[Integer]] = mapped_column(Integer)
    guid: Mapped[Optional[String]] = mapped_column(String)
    in_progress: Mapped[Optional[String]] = mapped_column(String)
    instance: Mapped[Optional[String]] = mapped_column(String)
    instance_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    is_default: Mapped[Optional[Integer]] = mapped_column(Integer)
    job_mode: Mapped[Optional[String]] = mapped_column(String)
    job_version: Mapped[Optional[String]] = mapped_column(String)
    last_file: Mapped[Optional[Integer]] = mapped_column(Integer)
    last_update: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    load_method: Mapped[Optional[Integer]] = mapped_column(Integer)
    metadata_buffer_size: Mapped[Optional[Integer]] = mapped_column(Integer)
    metadata_io: Mapped[Optional[Integer]] = mapped_column(Integer)
    name: Mapped[Optional[String]] = mapped_column(String)
    object_int_oid: Mapped[Optional[String]] = mapped_column(String)
    object_long_name: Mapped[Optional[String]] = mapped_column(String)
    object_name: Mapped[Optional[String]] = mapped_column(String)
    object_number: Mapped[Optional[Integer]] = mapped_column(Integer)
    object_path_seqno: Mapped[Optional[Integer]] = mapped_column(Integer)
    object_row: Mapped[Optional[Integer]] = mapped_column(Integer)
    object_schema: Mapped[Optional[String]] = mapped_column(String)
    object_tablespace: Mapped[Optional[String]] = mapped_column(String)
    object_type: Mapped[Optional[String]] = mapped_column(String)
    object_type_path: Mapped[Optional[String]] = mapped_column(String)
    objnum: Mapped[Optional[Integer]] = mapped_column(Integer)
    old_value: Mapped[Optional[String]] = mapped_column(String)
    operation: Mapped[Optional[String]] = mapped_column(String)
    option_tag: Mapped[Optional[String]] = mapped_column(String)
    orig_base_object_name: Mapped[Optional[String]] = mapped_column(String)
    orig_base_object_schema: Mapped[Optional[String]] = mapped_column(String)
    original_object_name: Mapped[Optional[String]] = mapped_column(String)
    original_object_schema: Mapped[Optional[String]] = mapped_column(String)
    packet_number: Mapped[Optional[Integer]] = mapped_column(Integer)
    parallelization: Mapped[Optional[Integer]] = mapped_column(Integer)
    parent_object_name: Mapped[Optional[String]] = mapped_column(String)
    parent_object_schema: Mapped[Optional[String]] = mapped_column(String)
    parent_process_order: Mapped[Optional[Integer]] = mapped_column(Integer)
    partition_name: Mapped[Optional[String]] = mapped_column(String)
    phase: Mapped[Optional[Integer]] = mapped_column(Integer)
    platform: Mapped[Optional[String]] = mapped_column(String)
    processing_state: Mapped[Optional[String]] = mapped_column(String)
    processing_status: Mapped[Optional[String]] = mapped_column(String)
    process_name: Mapped[Optional[String]] = mapped_column(String)
    process_order: Mapped[Optional[Integer]] = mapped_column(Integer)
    property: Mapped[Optional[Integer]] = mapped_column(Integer)
    proxy_schema: Mapped[Optional[String]] = mapped_column(String)
    proxy_view: Mapped[Optional[String]] = mapped_column(String)
    queue_tabnum: Mapped[Optional[Integer]] = mapped_column(Integer)
    remote_link: Mapped[Optional[String]] = mapped_column(String)
    scn: Mapped[Optional[Integer]] = mapped_column(Integer)
    seed: Mapped[Optional[Integer]] = mapped_column(Integer)
    service_name: Mapped[Optional[String]] = mapped_column(String)
    size_estimate: Mapped[Optional[Integer]] = mapped_column(Integer)
    src_compat: Mapped[Optional[String]] = mapped_column(String)
    start_time: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    state: Mapped[Optional[String]] = mapped_column(String)
    status_queue: Mapped[Optional[String]] = mapped_column(String)
    subpartition_name: Mapped[Optional[String]] = mapped_column(String)
    target_xml_clob: Mapped[Optional[String]] = mapped_column(String)
    tde_rewrapped_key: Mapped[Optional[String]] = mapped_column(String)
    template_table: Mapped[Optional[String]] = mapped_column(String)
    timezone: Mapped[Optional[String]] = mapped_column(String)
    total_bytes: Mapped[Optional[Integer]] = mapped_column(Integer)
    trigflag: Mapped[Optional[Integer]] = mapped_column(Integer)
    unload_method: Mapped[Optional[Integer]] = mapped_column(Integer)
    user_directory: Mapped[Optional[String]] = mapped_column(String)
    user_file_name: Mapped[Optional[String]] = mapped_column(String)
    user_name: Mapped[Optional[String]] = mapped_column(String)
    value_n: Mapped[Optional[Integer]] = mapped_column(Integer)
    value_t: Mapped[Optional[String]] = mapped_column(String)
    version: Mapped[Optional[Integer]] = mapped_column(Integer)
    work_item: Mapped[Optional[String]] = mapped_column(String)
    xml_clob: Mapped[Optional[String]] = mapped_column(String)
    xml_process_order: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)