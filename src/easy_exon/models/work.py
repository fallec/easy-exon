from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class LaborCost(BaseModel):
    """Сводная запись о план-фактных трудозатратах (список в `laborCosts`)."""
    date: date
    planWorkers: int
    factWorkers: Optional[int] = None
    delta: Optional[int] = None


class CompletedVolume(BaseModel):
    """Фиксация выполненного объёма работ."""
    volume: Decimal
    date: date
    author: str
    comment: Optional[str] = None
    modifiedAt: datetime
    volumeId: str


class PlanLaborCost(BaseModel):
    """Планируемое количество рабочих на диапазон дат."""
    id: str
    numberOfWorkers: int
    startDate: date
    endDate: date
    modifiedAt: datetime


class FactLaborCost(BaseModel):
    """Фактические трудозатраты за день (workers * hours)."""
    id: str
    numberOfWorkers: int
    date: date
    duration: int
    profession: Optional[str] = None
    author: str
    timeSpent: int
    modifiedAt: datetime


class WorkModel(BaseModel):
    """Расширенная модель работы/этапа проекта."""

    # ─── Минимум ───
    id: str

    # ─── Структура и положение в иерархии ───
    parent: Optional[str] = None
    fullPath: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None                # WORK / TOTAL_WORK / …
    graphId: Optional[str] = None
    code: Optional[int] = None
    sortOrder: Optional[int] = None
    categoryId: Optional[str] = None

    # ─── Организации и участники ───
    executorOrgId: Optional[str] = None
    editors: List[str] = Field(default_factory=list)
    responsible: List[str] = Field(default_factory=list)

    # ─── Базовые даты ───
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    fact_start_date: Optional[date] = None
    fact_end_date: Optional[date] = None
    base_start_date: Optional[date] = None
    base_end_date: Optional[date] = None
    contract_start_date: Optional[date] = None
    contract_end_date: Optional[date] = None
    min_start_date: Optional[date] = None
    deadline: Optional[date] = None
    projectedCompletionDate: Optional[date] = None

    # ─── Производственные показатели ───
    planVolume: Optional[Decimal] = None
    remainingVolume: Optional[Decimal] = None
    remainingPrice: Optional[Decimal] = None
    remainingProgressVolume: Optional[float] = None
    productionRate: Optional[float] = None
    laborIntensity: Optional[float] = None
    unitMeasure: Optional[str] = None
    unitPrice: Optional[Decimal] = None
    profession: Optional[Dict[str, int]] = None

    # ─── Длительности ───
    durationByDates: Optional[int] = None
    durationByBaseDates: Optional[int] = None
    durationByFactDates: Optional[int] = None

    # ─── Прогресс и отклонения ───
    progressByDates: Optional[float] = None
    progressByBaseDates: Optional[float] = None
    actualProgress: Optional[float] = None
    progress: Optional[float] = None
    volumeProgressProportionByDates: Optional[float] = None
    volumeProgressProportionByBaseDates: Optional[float] = None
    planProgressProportion: Optional[float] = None
    planFactProgressProportionByDates: Optional[float] = None
    planFactProgressDeviationByCompletion: Optional[float] = None
    deviationByStartingOfBasePlan: Optional[float] = None
    deviationByEndingOfBasePlan: Optional[float] = None
    deviationByBaseEndDate: Optional[float] = None
    projectedCompletionDateDeviation: Optional[int] = None
    remainingToProjectedCompletionDate: Optional[int] = None
    tempByEndDate: Optional[int] = None
    tempByBaseEndDate: Optional[int] = None

    # ─── Денежные метрики (опционально все Decimal/float) ───
    totalCost: Optional[Decimal] = None
    currentCost: Optional[Decimal] = None
    currentCostProportion: Optional[float] = None
    currentCostByDates: Optional[Decimal] = None
    currentCostProportionByDates: Optional[float] = None
    currentCostByBaseDates: Optional[Decimal] = None
    currentCostProportionByBaseDates: Optional[float] = None
    planFactCostDeviationByBaseDates: Optional[Decimal] = None
    planFactCostProportionByBaseDates: Optional[float] = None
    planFactCostDeviationByCompletionByDates: Optional[Decimal] = None
    planFactCostProportionByCompletionByDates: Optional[float] = None

    # ─── BIM / документы ───
    bimModelIds: Optional[List[str]] = None
    bimModel: Optional[Any] = None
    documents: List[Any] = Field(default_factory=list)

    # ─── Коллекции вложенных структур ───
    laborCosts: List[LaborCost] = Field(default_factory=list)
    planLaborCosts: List[PlanLaborCost] = Field(default_factory=list)
    factLaborCosts: List[FactLaborCost] = Field(default_factory=list)
    completedVolumes: List[CompletedVolume] = Field(default_factory=list)
    planVolumes: List[Any] = Field(default_factory=list)

    # ─── Прочее ───
    backlogStatus: Optional[int] = None
    fixedPlanLabor: Optional[bool] = None
    errors: Dict[str, Any] = Field(default_factory=dict)
    comment: Optional[str] = None
    budget: Optional[Any] = None

    class Config:
        extra = "allow"
        anystr_strip_whitespace = True
        orm_mode = True
