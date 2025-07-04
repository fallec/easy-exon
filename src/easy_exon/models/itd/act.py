from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class ItdDocumentSetTask(BaseModel):
    id: str
    name: Optional[str] = None
    documentStatus: Optional[str] = None

    class Config:
        extra = "allow"


class SupportDocument(BaseModel):
    fileId: str

    date: Optional[str] = None
    documentName: Optional[str] = None
    extension: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    executiveSchemeId: Optional[str] = None
    isActual: Optional[bool] = None
    itdDocumentId: Optional[str] = None
    explorerEntityId: Optional[str] = None
    workDocumentId: Optional[str] = None
    workDocumentOriginalFileId: Optional[str] = None
    fileIdWithStamp: Optional[str] = None
    number: Optional[str] = None
    orgName: Optional[str] = None
    createdBy: Optional[str] = None
    successSigned: Optional[bool] = None
    change: Optional[str] = None
    vprDate: Optional[str] = None
    cipher: Optional[str] = None
    numberList: Optional[str] = None
    absoluteNumberList: Optional[str] = None
    inherit: Optional[bool] = None
    generate: Optional[bool] = None
    registryDocsCountMap: Optional[Dict[str, Any]] = None
    actualVolumes: Optional[Any] = None
    fullDocumentName: Optional[str] = None
    shouldAddTitlePages: Optional[bool] = None
    startPage: Optional[int] = None
    isAllPagesSelected: Optional[bool] = None
    gipApproves: Optional[Any] = None
    authorWorkDoc: Optional[str] = None
    isCustomPagesList: Optional[bool] = None
    workDocumentOriginalFileIdOrFileId: Optional[str] = None

    class Config:
        extra = "allow"


class ActModel(BaseModel):
    id: str

    version: Optional[int] = None
    executorId: Optional[str] = None
    currentExecutorId: Optional[str] = None
    currentExecutor: Optional[str] = None
    author: Optional[str] = None
    executorOrganizationId: Optional[str] = None
    documentStatus: Optional[str] = None
    projectId: Optional[str] = None
    sendDate: Optional[str] = None
    deleted: Optional[bool] = None
    docType: Optional[str] = None
    actNum: Optional[str] = None
    actDate: Optional[str] = None
    actName: Optional[str] = None
    commentsCount: Optional[int] = None
    description: Optional[str] = None
    sectionId: Optional[str] = None
    sectionName: Optional[str] = None
    itdDocumentType: Optional[str] = None
    isActual: Optional[bool] = None
    indicatorForFilter: Optional[bool] = None
    orgId: Optional[str] = None
    userId: Optional[str] = None
    itdDocumentSetTaskList: Optional[List[ItdDocumentSetTask]] = None

    class Config:
        extra = "allow"


class ActDetailModel(ActModel):
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    fileId: Optional[str] = None
    name: Optional[str] = None
    permissibleLoad: Optional[Any] = None
    sectionAndSubsectionName: Optional[str] = None
    partName: Optional[str] = None
    documentSet: Optional[Any] = None
    cipher: Optional[str] = None
    receiptDate: Optional[str] = None
    actionDate: Optional[str] = None
    approvalDate: Optional[str] = None
    transferForReworkDate: Optional[str] = None
    transferToClientDate: Optional[str] = None
    vprExpirationDays: Optional[int] = None
    isrTaskId: Optional[str] = None
    wayBillFileId: Optional[str] = None
    pdfFileId: Optional[str] = None
    changedPDFFileId: Optional[str] = None
    zipFileId: Optional[str] = None
    note: Optional[str] = None
    history: Optional[List[Any]] = None
    pirStatus: Optional[str] = None
    processStarted: Optional[bool] = None
    canceled: Optional[bool] = None
    url: Optional[str] = None
    instanceCount: Optional[int] = None
    status: Optional[str] = None
    generalWorkIds: Optional[Any] = None
    workTypeId: Optional[str] = None
    workTypeIds: Optional[List[str]] = None
    materialList: Optional[Any] = None
    signerIds: Optional[Any] = None
    checkerIds: Optional[Any] = None
    reviewerIds: Optional[Any] = None
    comment: Optional[bool] = None
    formJsonId: Optional[str] = None
    subsequentWorks: Optional[Any] = None
    supportDocuments: Optional[List[SupportDocument]] = None
    construction: Optional[Any] = None
    loadPercent: Optional[int] = None
    loadPermission: Optional[Any] = None
    workPermission: Optional[Any] = None
    descriptionFromGeneralJournal: Optional[str] = None
    anotherPeoples: Optional[Any] = None
    signerInfoId: Optional[str] = None
    hasReportRegister: Optional[Any] = None
    approversInfoId: Optional[str] = None
    documentType: Optional[str] = None
    reportRegistryDocId: Optional[str] = None
    aosrIds: Optional[List[str]] = None
    additionalInformation: Optional[Any] = None
    reformWithSameVersion: Optional[bool] = None
    actualVolumes: Optional[Any] = None
    executiveSchemeActualVolumes: Optional[Any] = None
    actFormType: Optional[str] = None
    signer: Optional[str] = None
    sodSendingStatus: Optional[str] = None
    documentName: Optional[str] = None
    documentId: Optional[str] = None
    newRouteIntegrationAct: Optional[bool] = None

    class Config:
        extra = "allow"
