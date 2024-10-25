from django.shortcuts import get_object_or_404, render, redirect
from .forms import HouseholdForm, HouseholdMemberForm
from .models import Household, HouseholdMember
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required

def create_household_member(request, household_id):
    # Retrieve the household by ID
    household = get_object_or_404(Household, id=household_id)
    
    if request.method == 'POST':
        form = HouseholdMemberForm(request.POST)
        if form.is_valid():
            # Save the form but don't commit to the database yet
            household_member = form.save(commit=False)
            # Assign the household to the household_member
            household_member.household = household
            # Save the household_member
            household_member.save()
            # Redirect to the household member list
            return redirect('household_member_list')
    else:
        form = HouseholdMemberForm()
    
    return render(request, 'create_household_member.html', {'form': form, 'household': household})








@login_required
def create_household(request):
    if request.method == 'POST':
        household_form = HouseholdForm(request.POST)
        member_form = HouseholdMemberForm(request.POST)

        if household_form.is_valid() and member_form.is_valid():
            household = household_form.save()
            member = member_form.save(commit=False)
            member.household = household
            member.save()
            return redirect('household_list')
    else:
        household_form = HouseholdForm()
        member_form = HouseholdMemberForm()

    return render(request, 'create_household.html', {
        'household_form': household_form,
        'member_form': member_form,
    })

def household_list(request):
    query = request.GET.get('query', '')
    selected_mahallu_area = request.GET.get('mahallu_area', '')
    selected_head_of_household = request.GET.get('head_of_household', '')

    households = Household.objects.all()

    # Filter households based on query
    if query:
        households = households.filter(house_name__icontains=query)

    if selected_mahallu_area:
        households = households.filter(mahallu_area=selected_mahallu_area)

    if selected_head_of_household:
        households = households.filter(head_of_household=selected_head_of_household)

    # Get unique Mahallu Areas and Heads of Household for the filter dropdowns
    mahallu_areas = households.values_list('mahallu_area', flat=True).distinct()
    household_heads = households.values_list('head_of_household', flat=True).distinct()

    context = {
        'households': households,
        'query': query,
        'selected_mahallu_area': selected_mahallu_area,
        'selected_head_of_household': selected_head_of_household,
        'mahallu_areas': mahallu_areas,
        'household_heads': household_heads,
    }

    return render(request, 'household_list.html', context)
def edit_household(request, pk):
    household = get_object_or_404(Household, pk=pk)
    if request.method == 'POST':
        form = HouseholdForm(request.POST, instance=household)
        if form.is_valid():
            form.save()
            return redirect('household_list')
    else:
        form = HouseholdForm(instance=household)
    return render(request, 'edit_household.html', {'form': form})

def delete_household(request, pk):
    household = get_object_or_404(Household, pk=pk)
    if request.method == 'POST':
        household.delete()
        return redirect('household_list')
    return render(request, 'confirm_delete.html', {'household': household})

def household_member_list(request):
    search_name = request.GET.get('search_name', '')
    selected_relationship = request.GET.get('relationship_to_head', '')
    selected_job = request.GET.get('job', '')

    members = HouseholdMember.objects.all()

    # Apply filters based on user input
    if search_name:
        members = members.filter(name__icontains=search_name)

    if selected_relationship:
        members = members.filter(relationship_to_head=selected_relationship)

    if selected_job:
        members = members.filter(job=selected_job)

    # Get distinct values for filtering
    relationships = HouseholdMember.objects.values_list('relationship_to_head', flat=True).distinct()
    jobs = HouseholdMember.objects.values_list('job', flat=True).distinct()

    return render(request, 'household_member_list.html', {
        'members': members,
        'relationships': relationships,
        'jobs': jobs,
    })
def edit_household_member(request, pk):
    member = get_object_or_404(HouseholdMember, pk=pk)
    if request.method == 'POST':
        form = HouseholdMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('household_member_list')
    else:
        form = HouseholdMemberForm(instance=member)
    return render(request, 'edit_household_member.html', {'form': form})

def delete_household_member(request, pk):
    member = get_object_or_404(HouseholdMember, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('household_member_list')
    return render(request, 'confirm_delete_member.html', {'member': member})





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Redirect to create household form instead of household list
            return redirect('create_household')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')



